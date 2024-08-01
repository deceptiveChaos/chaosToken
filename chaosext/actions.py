# -*- coding: utf-8 -*-
import paramiko
import pathlib
import random

__all__ = [
    'create_local_files',
    'send_file_over_ssh',
    'create_and_send_files'
]

"""def create_local_file(file_path: str, file_content: str) -> str:
    file_dir = pathlib.Path(file_path).parent
    if not file_dir.exists():
        file_dir.mkdir(parents=True)
    with open(file_path, 'w') as f:
        f.write(file_content)
    return file_path"""

def create_local_files(folder_path: pathlib.Path) -> list:
    files = []
    for file in folder_path.iterdir():
        files.append(file)
    return files

def send_file_over_ssh(
    file_path: str, 
    host: str, 
    username: str, 
    password: str
) -> None:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(
            hostname=host, 
            username=username, 
            password=password
        )
        sftp = ssh.open_sftp()
        sftp.put(file_path, file_path)
    finally:
        ssh.close()

def create_and_send_files(
    folder_path: pathlib.Path, 
    host: str, 
    username: str, 
    password: str, 
    remote_folder: pathlib.Path
) -> None:
    files = create_local_files(folder_path)
    # Randomly select the number of files to send
    num_files_to_send = random.randint(1, len(files))
    # Randomly select the files to send
    files_to_send = random.sample(files, num_files_to_send)  
    
    for file in files_to_send:
        remote_file_path = remote_folder / file.name
        send_file_over_ssh(
            file, 
            host, 
            username, 
            password, 
            remote_file_path
            )