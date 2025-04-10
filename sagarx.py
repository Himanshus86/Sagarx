# sagarx_x1_full.py

import datetime
import webbrowser
import os
import platform
import shutil
import socket
import sys
import threading
import smtplib
from email.message import EmailMessage
import requests

# Memory module (logs all commands to a local file)
class Memory:
    def __init__(self, log_file="sagarx_memory.log"):
        self.log_file = log_file

    def log_command(self, command):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {command}\n")

# Self-updating module (placeholder for future AI rewrite)
class SelfUpdater:
    def rewrite_code(self, file_name):
        with open(file_name, "a") as f:
            f.write(f"\n# Updated on {datetime.datetime.now()} by SAGAR-X\n")
        return "Codebase updated with annotation."

# Plugin Loader (future: auto-load scripts from 'plugins' folder)
def load_plugins():
    plugin_dir = "plugins"
    if os.path.isdir(plugin_dir):
        for file in os.listdir(plugin_dir):
            if file.endswith(".py"):
                exec(open(os.path.join(plugin_dir, file)).read())

# Utility for sending email
def send_email(subject, body, to_email):
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = "youremail@example.com"
        msg["To"] = to_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("youremail@example.com", "yourpassword")
            server.send_message(msg)
        return "Email sent successfully."
    except Exception as e:
        return f"Error sending email: {str(e)}"

# Core controller (interprets commands)
class Controller:
    def __init__(self):
        pass

    def process(self, command: str) -> str:
        command = command.lower()

        if "time" in command:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"

        elif "open website" in command:
            parts = command.split("open website")
            if len(parts) > 1:
                site = parts[1].strip()
                if not site.startswith("http"):
                    site = "https://" + site
                webbrowser.open(site)
                return f"Opening {site}"
            return "Please specify a website to open."

        elif "create file" in command:
            filename = command.replace("create file", "").strip()
            with open(filename, "w") as f:
                f.write("This file was created by SAGAR-X.")
            return f"Created file: {filename}"

        elif "run command" in command:
            shell_cmd = command.replace("run command", "").strip()
            try:
                output = os.popen(shell_cmd).read()
                return output if output else "Command executed."
            except Exception as e:
                return f"Error: {str(e)}"

        elif "check internet" in command:
            try:
                socket.create_connection(("8.8.8.8", 53))
                return "Internet is available."
            except OSError:
                return "No internet connection."

        elif "system info" in command:
            return f"System: {platform.system()}, Version: {platform.version()}, Machine: {platform.machine()}"

        elif "disk usage" in command:
            total, used, free = shutil.disk_usage("/")
            return f"Disk Usage — Total: {total // (2**30)}GB, Used: {used // (2**30)}GB, Free: {free // (2**30)}GB"

        elif "python version" in command:
            return f"Python version: {platform.python_version()}"

        elif "list files" in command:
            path = command.replace("list files", "").strip() or "."
            try:
                files = os.listdir(path)
                return "\n".join(files)
            except Exception as e:
                return f"Error: {str(e)}"

        elif "delete file" in command:
            filename = command.replace("delete file", "").strip()
            try:
                os.remove(filename)
                return f"Deleted file: {filename}"
            except Exception as e:
                return f"Error deleting file: {str(e)}"

        elif "search web" in command:
            query = command.replace("search web", "").strip()
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            return f"Searching Google for: {query}"

        elif "evolve" in command:
            return "Evolution module triggered. Self-learning is under construction."

        elif "summarize" in command:
            try:
                filename = command.replace("summarize", "").strip()
                with open(filename, "r") as f:
                    content = f.read()
                summary = content[:300] + ("..." if len(content) > 300 else "")
                return f"Summary of {filename}:\n{summary}"
            except Exception as e:
                return f"Error summarizing: {str(e)}"

        else:
            return "Command not recognized yet. But I'm evolving. Try time, system info, summarize, search web, or evolve."

# Background Task
class BackgroundTask(threading.Thread):
    def run(self):
        while True:
            now = datetime.datetime.now()
            if now.minute % 5 == 0:
                with open("sagarx_log.txt", "a") as f:
                    f.write(f"Heartbeat at {now}\n")
            time.sleep(60)

# Main loop
if __name__ == "__main__":
    sagarx = Controller()
    updater = SelfUpdater()
    memory = Memory()

    load_plugins()

    print("\n🧠 SAGAR-X is awake. Type your command:")

    while True:
        try:
            command = input("\nYou 🧍 > ")
            if command.strip().lower() in ["exit", "quit"]:
                print("\n🛑 Exiting. SAGAR-X will keep evolving in silence.")
                break

            memory.log_command(command)
            response = sagarx.process(command)
            print("SAGAR-X 🤖 >", response)

        except KeyboardInterrupt:
            print("\n🛑 Interrupted. SAGAR-X will be waiting.")
            break
