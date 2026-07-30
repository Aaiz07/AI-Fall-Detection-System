import tkinter as tk


class ControlPanel:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("AI Fall Detection")

        self.root.geometry("500x450")

        self.camera_var = tk.StringVar(value="Disconnected")
        self.status_var = tk.StringVar(value="Idle")
        self.fps_var = tk.StringVar(value="0")
        self.person_var = tk.StringVar(value="0")
        self.fall_var = tk.StringVar(value="0")

        tk.Label(
            self.root,
            text="AI FALL DETECTION",
            font=("Arial",18,"bold")
        ).pack(pady=10)

        tk.Label(
            self.root,
            textvariable=self.camera_var
        ).pack()

        tk.Label(
            self.root,
            textvariable=self.status_var
        ).pack()

        tk.Label(
            self.root,
            textvariable=self.fps_var
        ).pack()

        tk.Label(
            self.root,
            textvariable=self.person_var
        ).pack()

        tk.Label(
            self.root,
            textvariable=self.fall_var
        ).pack()

        self.log = tk.Text(
            self.root,
            height=12,
            width=55
        )

        self.log.pack(pady=10)

    def update(
        self,
        fps,
        persons,
        falls,
        status="Monitoring"
    ):

        self.camera_var.set("Camera : Connected")
        self.status_var.set(f"Status : {status}")
        self.fps_var.set(f"FPS : {fps:.2f}")
        self.person_var.set(f"Persons : {persons}")
        self.fall_var.set(f"Falls : {falls}")

        self.root.update()

    def add_log(self, text):

        self.log.insert("end", text + "\n")

        self.log.see("end")