"""Small shared Tk interface for the individual and integrated Wells tools."""

from __future__ import annotations

import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .core import RenPyToolsError, run_operation


BG = "#222222"
FG = "#eeeeee"


class RenPyLocalizationFrame(tk.Frame):
    def __init__(self, master, *, initial_project="", initial_sdk=""):
        super().__init__(master, bg=BG, padx=14, pady=12)
        self.events = queue.Queue()
        self.busy = False
        self.sdk_var = tk.StringVar(value=initial_sdk)
        self.project_var = tk.StringVar(value=initial_project)
        self.language_var = tk.StringVar(value="brazil")
        self.status_var = tk.StringVar(value="Selecione o SDK e a pasta do jogo.")
        self.empty_var = tk.BooleanVar(value=True)
        self.format_var = tk.StringVar(value="tab")
        self.strings_var = tk.BooleanVar(value=False)
        self.notags_var = tk.BooleanVar(value=False)
        self.escape_var = tk.BooleanVar(value=False)
        self._build()
        self.after(100, self._poll_events)

    def _build(self):
        self.grid_columnconfigure(1, weight=1)
        tk.Label(self, text="WELLS · FERRAMENTAS REN’PY", bg=BG, fg="#ff3030",
                 font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 10))

        self._path_row(1, "SDK Ren’Py 8.5.3", self.sdk_var, self._browse_sdk)
        self._path_row(2, "Pasta do jogo", self.project_var, self._browse_project)

        tk.Label(self, text="Idioma / localização", bg=BG, fg=FG).grid(row=3, column=0, sticky="w", pady=5)
        self.language_entry = ttk.Entry(self, textvariable=self.language_var, width=28)
        self.language_entry.grid(row=3, column=1, columnspan=2, sticky="ew", pady=5)

        ttk.Separator(self).grid(row=4, column=0, columnspan=3, sticky="ew", pady=8)
        tk.Label(self, text="Gerar traduções", bg=BG, fg=FG,
                 font=("Segoe UI", 10, "bold")).grid(row=5, column=0, columnspan=3, sticky="w")
        self.empty_check = ttk.Checkbutton(self, text="Gerar strings vazias", variable=self.empty_var)
        self.empty_check.grid(row=6, column=0, columnspan=3, sticky="w", pady=(3, 7))
        self.generate_button = ttk.Button(self, text="Gerar estrutura de tradução", command=self._generate)
        self.generate_button.grid(row=7, column=0, columnspan=3, sticky="ew", pady=(0, 10))

        ttk.Separator(self).grid(row=8, column=0, columnspan=3, sticky="ew", pady=8)
        tk.Label(self, text="Extrair diálogos e strings", bg=BG, fg=FG,
                 font=("Segoe UI", 10, "bold")).grid(row=9, column=0, columnspan=3, sticky="w")
        tk.Label(self, text="Arquivo", bg=BG, fg=FG).grid(row=10, column=0, sticky="w", pady=4)
        self.format_box = ttk.Combobox(self, textvariable=self.format_var, values=("tab", "txt"),
                                       state="readonly", width=10)
        self.format_box.grid(row=10, column=1, sticky="w", pady=4)
        tk.Label(self, text="tab = tabela com contexto; txt = texto", bg=BG, fg="#bbbbbb").grid(
            row=10, column=2, sticky="w", padx=(8, 0), pady=4)
        self.strings_check = ttk.Checkbutton(self, text="Incluir todas as strings traduzíveis",
                                              variable=self.strings_var)
        self.strings_check.grid(row=11, column=0, columnspan=3, sticky="w")
        self.tags_check = ttk.Checkbutton(self, text="Remover tags de texto",
                                           variable=self.notags_var)
        self.tags_check.grid(row=12, column=0, columnspan=3, sticky="w")
        self.escape_check = ttk.Checkbutton(self, text="Escapar aspas e caracteres especiais",
                                             variable=self.escape_var)
        self.escape_check.grid(row=13, column=0, columnspan=3, sticky="w")
        self.extract_button = ttk.Button(self, text="Extrair diálogos", command=self._extract)
        self.extract_button.grid(row=14, column=0, columnspan=3, sticky="ew", pady=(6, 9))

        self.status = tk.Label(self, textvariable=self.status_var, bg=BG, fg="#d4d4d4",
                               anchor="w", justify="left", wraplength=560)
        self.status.grid(row=15, column=0, columnspan=3, sticky="ew", pady=(2, 5))
        self.progress = ttk.Progressbar(self, mode="indeterminate")
        self.progress.grid(row=16, column=0, columnspan=3, sticky="ew")
        tk.Label(self, text="O engine Ren’Py lê o projeto; os arquivos-fonte .rpy não são editados.",
                 bg=BG, fg="#aaaaaa", font=("Segoe UI", 8)).grid(row=17, column=0, columnspan=3,
                                                                  sticky="w", pady=(8, 0))

    def _path_row(self, row, label, variable, command):
        tk.Label(self, text=label, bg=BG, fg=FG).grid(row=row, column=0, sticky="w", pady=5)
        entry = ttk.Entry(self, textvariable=variable)
        entry.grid(row=row, column=1, sticky="ew", pady=5, padx=(0, 6))
        button = ttk.Button(self, text="Procurar…", command=command)
        button.grid(row=row, column=2, sticky="ew", pady=5)
        if not hasattr(self, "_buttons"):
            self._buttons = []
        self._buttons.append(button)

    def _browse_sdk(self):
        path = filedialog.askdirectory(title="Selecione a pasta do Ren’Py SDK")
        if path:
            self.sdk_var.set(path)

    def _browse_project(self):
        path = filedialog.askdirectory(title="Selecione a pasta raiz do jogo")
        if path:
            self.project_var.set(path)

    def _generate(self):
        self._start("generate")

    def _extract(self):
        self._start("extract")

    def _start(self, operation):
        if self.busy:
            return
        options = {
            "empty_strings": self.empty_var.get(),
            "dialogue_format": self.format_var.get(),
            "include_strings": self.strings_var.get(),
            "strip_tags": self.notags_var.get(),
            "escape_special": self.escape_var.get(),
        }
        self._set_busy(True)
        self.status_var.set("Executando o comando Ren’Py…")

        def worker():
            try:
                result = run_operation(
                    self.sdk_var.get(), self.project_var.get(), operation,
                    self.language_var.get(), **options,
                )
                self.events.put(("result", result))
            except Exception as exc:
                self.events.put(("error", exc))

        threading.Thread(target=worker, daemon=True).start()

    def _set_busy(self, busy):
        self.busy = busy
        state = "disabled" if busy else "normal"
        for button in [*getattr(self, "_buttons", []), self.generate_button, self.extract_button]:
            button.configure(state=state)
        for widget in (self.language_entry, self.format_box, self.empty_check,
                       self.strings_check, self.tags_check, self.escape_check):
            widget.configure(state=state)
        if busy:
            self.progress.start(10)
        else:
            self.progress.stop()

    def _poll_events(self):
        try:
            while True:
                kind, value = self.events.get_nowait()
                self._set_busy(False)
                if kind == "error":
                    self.status_var.set("Falha ao executar a operação.")
                    messagebox.showerror("Wells · Ren’Py", str(value), parent=self.winfo_toplevel())
                else:
                    outputs = "\n".join(str(p) for p in value.outputs)
                    if value.returncode == 0:
                        self.status_var.set(f"Concluído. Saída esperada:\n{outputs}")
                        messagebox.showinfo("Wells · Ren’Py", f"Operação concluída.\n\nSaída:\n{outputs}",
                                            parent=self.winfo_toplevel())
                    else:
                        details = (value.stderr or value.stdout or "Sem detalhes fornecidos pelo Ren’Py.").strip()
                        self.status_var.set(f"Ren’Py terminou com código {value.returncode}.")
                        messagebox.showerror("Wells · Ren’Py",
                                             f"O comando terminou com código {value.returncode}.\n\n{details[-4000:]}",
                                             parent=self.winfo_toplevel())
        except queue.Empty:
            pass
        self.after(100, self._poll_events)


def run_standalone():
    root = tk.Tk()
    root.title("Wells · Ferramentas Ren’Py")
    root.configure(bg=BG)
    root.minsize(650, 510)
    root.geometry("740x570")
    RenPyLocalizationFrame(root).pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    run_standalone()
