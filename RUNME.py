import subprocess
import sys, os
import re
import random
import time
import base64
import json

def decode_map_b64(encoded_data):
    """Decodes the Base64 string back into the Python dictionary."""
    decoded_bytes = base64.b64decode(encoded_data)
    decoded_string = decoded_bytes.decode('utf-8')
    # Use json.loads because the original dict uses "double quotes"
    return json.loads(decoded_string.replace("'", '"'))

OBFUSCATED_MAP_B64 = b'eyJSVlVOMjVDU0UxMzIiOiAiU1BBUlNISU5JIEIiLCAiUlZVTjI1Q1NFMTI4IjogIlNSSSBWQUlTSE5BVkkiLCAiUlZVTjI1Q1NFMTM4IjogIlNSSSBWQVNUSEFOIEJJTiIsICJSVlVOMjVDU0UxNDMiOiAiU1JJSEFSSSBZT0dBUFJBU0FEIiwgIlJWVU4yNUNTRTAxMyI6ICJTVURIQU5WQSBMQUtTSE1JIE5BUkFTSU1IQSIsICJSVlVOMjVDU0UwODYiOiAiU1VESElTSCBLUklTSE5BIEEiLCAiUlZVTjI1Q1NFMTkwIjogIlNVR05BQU4gUyBTSFlBTUFOVVIiLCAiUlZVTjI1Q1NFMDEwIjogIlNVSEFOSSBCIiwgIlJWVU4yNUNTRTI0OCI6ICJTVUhBTkkgUyBKRVdBUkdJIiwgIlJWVU4yNUNTRTEwMSI6ICJTVUpBWSBSIEsiLCAiUlZVTjI1Q1NFMzQxIjogIlNVTUFOIEJIQVQiLCAiUlZVTjI1Q1NFNDEzIjogIlNVTkFZQU5BIFYiLCAiUlZVTjI1Q1NFNDAzIjogIlNVTklMIEhBUklKQU4iLCAiUlZVTjI1Q1NFMjQ1IjogIlNVUkFKIEtVTUFSIiwgIlJWVU4yNUNTRTE3NCI6ICJTVVZFREEgRCIsICJSVlVOMjVDU0UwNjIiOiAiU1lFRCBPTUVSIEFITUVEIiwgIlJWVU4yNUNTRTA4NyI6ICJUQU5JU0ggU0FJS1JJU0hOQSBNVVJBSVNFVFRZIiwgIlJWVU4yNUNTRTAwMiI6ICJUQU5JU0hRIEpBSVNXQUwiLCAiUlZVTjI1Q1NFMTY0IjogIlRBTk1BWSBBTkFORCBQQVRUQU4iLCAiUlZVTjI1Q1NFMzE3IjogIlRBTlVKIEhBTFRJIiwgIlJWVU4yNUNTRTA2NSI6ICJUQU5VU0ggREVFUEFLIiwgIlJWVU4yNUNTRTA4MiI6ICJUQVJBTiBOIiwgIlJWVU4yNUNTRTA2NyI6ICJURUpBUyBMIEtBU1NIWUFQIiwgIlJWVU4yNUNTRTExMyI6ICJURUxVIE1PS1NISVRBIiwgIlJWVU4yNUNTRTA1OSI6ICJUSEFOVkkgSkFZQVJBTSIsICJSVlVOMjVDU0UwOTciOiAiVEhPVEFEQSBOSVRFRVNIIEtVTUFSIiwgIlJWVU4yNUNTRTIzNiI6ICJQVURBWSBLVU1BUiIsICJSVlVOMjVDU0UxNzYiOiAiVVRLQVJTSCBQUkFTQUQiLCAiUlZVTjI1Q1NFMjY1IjogIlVUU0FWIEhFR0RFIiwgIlJWVU4yNUNTRTEzMyI6ICJWIEJIVVZBTiIsICJSVlVOMjVDU0UzNjgiOiAiVlMgR1VSVSBURUpBU1dJIiwgIlJWVU4yNUNTRTM4MSI6ICJWQUlOQVZJIFZBSUJBViIsICJSVlVOMjVDU0UxNTQiOiAiVkFJU0hOQVZJIE1VUkFMSURIQVIgS1VMS0FSTkkiLCAiUlZVTjI1Q1NFMDMyIjogIlZBTlNIIEtBUE9PUiIsICJSVlVOMjVDU0UzMjciOiAiVkFSVU4gREVWQVJBSiIsICJSVlVOMjVDU0UxNjciOiAiVkFSVU4gR09XREEgTSIsICJSVlVOMjVDU0UwMzYiOiAiSEtSIEZMQUlHUkkiLCAiUlZVTjI1Q1NFMDAxIjogIlZFREFOVCBTQVhFTkEiLCAiUlZVTjI1Q1NFMTczIjogIlZFRElLQSBOQVlBTkEgQ0hPVkRFUiIsICJSVlVOMjVDU0UxOTIiOiAiVklCSEEgVklEWUEgTUFMWUFNIiwgIlJWVU4yNUNTRTE3MCI6ICJWSUtBUyBTUklOSVZBUyBWIiwgIlJWVU4yNUNTRTQxMSI6ICJWSUtBUyBZIFMiLCAiUlZVTjI1Q1NFMjg3IjogIlZJS1JBTSBIIiwgIlJWVU4yNUNTRTIwOCI6ICJWSU5BTVJBIEpBSU4iLCAiUlZVTjI1Q1NFMzE2IjogIlZJTk9EIEMuViIsICJSVlVOMjVDU0UxNjMiOiAiVklOVVRIQVMgUEFUSUwiLCAiUlZVTjI1Q1NFMzIzIjogIlZJU0hBTCIsICJSVlVOMjVDU0UxMDgiOiAiVklTSEVTSCBTSU5HSEFMIiwgIlJWVU4yNUNTRTI3OCI6ICJWSVNITlUgRyIsICJSVlVOMjVDU0UzMzAiOiAiVklTSFJVVEggVU1FU0giLCAiUlZVTjI1Q1NFMzg4IjogIlZJU0hSVVRIQSBWUyIsICJSVlVOMjVDU0UyNjAiOiAiVklWRUsgS0hFTkkiLCAiUlZVTjI1Q1NFMjA3IjogIlZJVkVLQU5BTkRBUkQiLCAiUlZVTjI1Q1NFMDc2IjogIllBU0ggSElSRU1BVEgiLCAiUlZVTjI1Q1NFMDI2IjogIllBU0hBUyBBIE1FUldBREUiLCAiUlZVTjI1Q1NFMTQ4IjogIllBU0hBUyBTIiwgIlJWVU4yNUNTRTMwNiI6ICJZQVNIV0FOVEggUyIsICJSVlVOMjVDU0UzNzgiOiAiWVVWQVJBSiBTIiwgIlJWVU4yNUNTRTI0MCI6ICJZVVZSQUogU0lOR0gifQ=='

USN_TO_NAME_MAP = decode_map_b64(OBFUSCATED_MAP_B64)
USN_TO_NAME_MAP = {usn: name.title() for usn, name in USN_TO_NAME_MAP.items()}

MULTILINE_COMMENT_PATTERN = re.compile(r'/\*[\s\S]*?\*/')
SINGLELINE_COMMENT_PATTERN = re.compile(r'//.*')


def get_usn_and_name() -> tuple[str, str]:
    while True:
        try:
            usn_input = input("Please enter the FULL USN (e.g., RVUN25CSE036): ").strip().upper()
            if not usn_input:
                print("USN cannot be empty.")
                continue
            if usn_input in USN_TO_NAME_MAP:
                default_name = USN_TO_NAME_MAP[usn_input]
                
                print(f"\n--- Confirmation for USN: {usn_input} ---")
                confirmation = input(
                    f"Found Name: {default_name}. Is this correct? [Y/n/new]: "
                ).strip().lower()

                if confirmation in ['y', 'yes', '']:
                    return usn_input, default_name
                
                elif confirmation in ['n', 'no', 'new']:
                    # User overrides the dictionary name
                    new_name = input("Please enter the correct name: ").strip()
                    if new_name:
                        return usn_input, new_name.title()
                    else:
                        print("Name cannot be empty. Please try again.")
                else:
                    print("Invalid input. Please enter 'y', 'n', or 'new'.")

            else:
                print(f"\nUSN '{usn_input}' not found in the list.")
                new_name = input("Please enter the student's full name: ").strip()
                if new_name:
                    return usn_input, new_name.title()
                else:
                    print("Name cannot be empty. Please enter the name.")

        except EOFError:
            print("\nNon-interactive input detected. Cannot proceed without USN and Name.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)


def remove_comments_from_file(filepath: str, usn: str, name: str):
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        cleaned_content = MULTILINE_COMMENT_PATTERN.sub('', content)
        cleaned_lines = []
        for line in cleaned_content.splitlines():
            line_no_comment = SINGLELINE_COMMENT_PATTERN.sub('', line, 1)
            cleaned_lines.append(line_no_comment)
        final_cleaned_content = '\n'.join([line for line in cleaned_lines if line.strip() != '']).strip()
        usn_line = f"// USN: {usn}"
        name_line = f"// Name: {name}"
        if random.choice([True, False]):
            header_comments = [usn_line, name_line]
        else:
            header_comments = [name_line, usn_line]
        header_content = '\n'.join(header_comments) + '\n'

        content_to_write = header_content + final_cleaned_content

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_to_write)
        print(f"[SUCCESS] Processed file: {filepath}")
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filepath}")
    except Exception as e:
        print(f"[ERROR] Failed to process file {filepath}: {e}")


def process_directory(directory_path: str, usn: str, name: str):
    print("-" * 30)
    print(f"Applying header for {name} ({usn}) to all .c files in: {os.path.abspath(directory_path)}")
    print("-" * 30)

    if not os.path.isdir(directory_path):
        print(f"[FATAL] Error: Directory not found at '{directory_path}'")
        return

    c_files_found = 0

    # os.walk yields (dirpath, dirnames, filenames)
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.c'):
                filepath = os.path.join(root, file)
                remove_comments_from_file(filepath, usn, name)
                c_files_found += 1

    print("-" * 30)
    if c_files_found == 0:
        print("No .c files found in the specified path or its subdirectories.")
    else:
        print(f"Finished processing {c_files_found} .c file(s).")
    print("-" * 30)


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.stdout:
            print("Output:\n", result.stdout)
            time.sleep(0.5)
        if result.stderr:
            print("There was a problem in your program, but do not worry, I am too smart for this.")
            run_command(command=command+" -lm")
            time.sleep(2)
    except Exception as e:
        print("Exception : ",e)
        
        
def compile_codes(start, end):
    os.makedirs("Output", exist_ok=True)
    for i in range(start, end + 1):
        command = f"gcc -o Output/Program{i} Program{i}.c"
        print(f"Compiling Program{i}.c ...")
        run_command(command)
    print("\nCompilation complete.")

if __name__ == "__main__":
    commands = [
        "chmod +x gap.sh",
        "./gap.sh"
    ]
    
    for command in commands:
        run_command(command)
        
    os.remove("gap.sh")
        
    try:
        target_usn, target_name = get_usn_and_name()
        if len(sys.argv) > 1:
            target_dir = sys.argv[1]
        else:
            target_dir = os.getcwd()
            print(f"\nNo directory path provided. Defaulting to current directory: {target_dir}")
        process_directory(target_dir, target_usn, target_name)
        
    except KeyboardInterrupt:
        print("\n\nOperation interrupted by user.")
        sys.exit(0)
    
    print("************COMPILE THE PROGRAMS************")
    end = int(input("Till which program: "))
    compile_codes(1,end)
    print("\n\n\n\n\n")
    print("\033[1m**************************\033[0m")
    print("\033[1mINITIALIZING SELF DESTRUCT\033[0m")
    print("\033[1m**************************\033[0m")
    print("\n\n\n\n\n")
    
    os.remove("RUNME.py")