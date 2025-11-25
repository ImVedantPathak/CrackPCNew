import subprocess
import sys, os
import re
import random
import time

USN_TO_NAME_MAP = { "RVUN25CSE132": "SPARSHINI B", "RVUN25CSE128": "SRI VAISHNAVI", "RVUN25CSE138": "SRI VASTHAN BIN", "RVUN25CSE143": "SRIHARI YOGAPRASAD", "RVUN25CSE013": "SUDHANVA LAKSHMI NARASIMHA", "RVUN25CSE086": "SUDHISH KRISHNA A", "RVUN25CSE190": "SUGNAAN S SHYAMANUR", "RVUN25CSE010": "SUHANI B", "RVUN25CSE248": "SUHANI S JEWARGI", "RVUN25CSE101": "SUJAY R K", "RVUN25CSE341": "SUMAN BHAT", "RVUN25CSE413": "SUNAYANA V", "RVUN25CSE403": "SUNIL HARIJAN", "RVUN25CSE245": "SURAJ KUMAR", "RVUN25CSE174": "SUVEDA D", "RVUN25CSE062": "SYED OMER AHMED", "RVUN25CSE087": "TANISH SAIKRISHNA MURAISETTY", "RVUN25CSE002": "TANISHQ JAISWAL", "RVUN25CSE164": "TANMAY ANAND PATTAN", "RVUN25CSE317": "TANUJ HALTI", "RVUN25CSE065": "TANUSH DEEPAK", "RVUN25CSE082": "TARAN N", "RVUN25CSE067": "TEJAS L KASSHYAP", "RVUN25CSE113": "TELU MOKSHITA", "RVUN25CSE059": "THANVI JAYARAM", "RVUN25CSE097": "THOTADA NITEESH KUMAR", "RVUN25CSE236": "PUDAY KUMAR", "RVUN25CSE176": "UTKARSH PRASAD", "RVUN25CSE265": "UTSAV HEGDE", "RVUN25CSE133": "V BHUVAN", "RVUN25CSE368": "VS GURU TEJASWI", "RVUN25CSE381": "VAINAVI VAIBAV", "RVUN25CSE154": "VAISHNAVI MURALIDHAR KULKARNI", "RVUN25CSE032": "VANSH KAPOOR", "RVUN25CSE327": "VARUN DEVARAJ", "RVUN25CSE167": "VARUN GOWDA M", "RVUN25CSE036": "HKR FLAIGRI", "RVUN25CSE001": "VEDANT SAXENA", "RVUN25CSE173": "VEDIKA NAYANA CHOVDER", "RVUN25CSE192": "VIBHA VIDYA MALYAM", "RVUN25CSE170": "VIKAS SRINIVAS V", "RVUN25CSE411": "VIKAS Y S", "RVUN25CSE287": "VIKRAM H", "RVUN25CSE208": "VINAMRA JAIN", "RVUN25CSE316": "VINOD C.V", "RVUN25CSE163": "VINUTHAS PATIL", "RVUN25CSE323": "VISHAL", "RVUN25CSE108": "VISHESH SINGHAL", "RVUN25CSE278": "VISHNU G", "RVUN25CSE330": "VISHRUTH UMESH", "RVUN25CSE388": "VISHRUTHA VS", "RVUN25CSE260": "VIVEK KHENI", "RVUN25CSE207": "VIVEKANANDARD", "RVUN25CSE076": "YASH HIREMATH", "RVUN25CSE026": "YASHAS A MERWADE", "RVUN25CSE148": "YASHAS S", "RVUN25CSE306": "YASHWANTH S", "RVUN25CSE378": "YUVARAJ S", "RVUN25CSE240": "YUVRAJ SINGH" }
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