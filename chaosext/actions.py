# -*- coding: utf-8 -*-
import paramiko
import pathlib
import random

__all__ = [
    'create_local_files',
    'send_file_over_ssh',
    'create_and_send_files'
]

def create_local_files(folder_path: str) -> list:
    folder_path = pathlib.Path(folder_path)
    files = []
    for file in folder_path.iterdir():
        files.append(file)
    return files

def send_file_over_ssh(
    file_path: str, 
    host: str, 
    username: str, 
    password: str, 
    remote_folder: str
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
        file_path = pathlib.Path(file_path)
        remote_file_path = str(pathlib.Path(remote_folder) / file_path.name)
        sftp.put(str(file_path), remote_file_path)
    finally:
        ssh.close()

def create_and_send_files(
    folder_path: str, 
    host: str, 
    username: str, 
    password: str, 
    remote_folder: str
) -> None:
    folder_path = pathlib.Path(folder_path)
    remote_folder = pathlib.Path(remote_folder)
    files = create_local_files(folder_path)
    # Randomly select the number of files to send
    num_files_to_send = random.randint(1, len(files))
    # Randomly select the files to send
    files_to_send = random.sample(files, num_files_to_send)  
    
    for file in files_to_send:
        send_file_over_ssh(
            str(file), 
            host, 
            username, 
            password, 
            str(remote_folder)
        )