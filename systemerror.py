def execute_code_from_file(file_path):
    try:
        with open(file_path,'r') as f:
            code=f.read()
            
        print("Executing The Code..\n")
        exec(code)
        
        
    except FileNotFoundError as e:
        print("Error:File not Found.Please Check the Path",e)
    except SystemError as se:
        print("SystenError Caught!")
        print(f"Details :{se}")
    except Exception as e:
        print("An Error Occured!")
        print(f"Details:{e}")
        
file_path=input("Enter The Path To Your Python Code File:")
execute_code_from_file(file_path)
        

