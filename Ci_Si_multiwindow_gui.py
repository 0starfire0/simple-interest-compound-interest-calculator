import tkinter as tk
window=tk.Tk()
window.title("Interest Calculator")
window.geometry("400x300")
def open_si_window():
    second = tk.Toplevel(window)
    second.title("Simple Interest ")
    second.geometry("400x300")
    tk.Label(second,text="SI Calculator").pack()
#principal
    tk.Label(second,text="Principal").pack()
    principal_entry=tk.Entry(second)
    principal_entry.pack()
#rate
    tk.Label(second,text="Rate(%)").pack()
    rate_entry= tk.Entry(second)
    rate_entry.pack()
#time
    tk.Label(second,text="Time").pack()
    time_entry=tk.Entry(second)
    time_entry.pack()
    result_label=tk.Label(second,text="")
    result_label.pack()
    #calculatingSI
    def calculate_si():
        p=float(principal_entry.get())
        r=float(rate_entry.get())
        t=float(time_entry.get())

        si=(p*r*t)/100
        result_label.config(text=f"Simple Interest = {si}")

    tk.Button(
        second,
        text="Calculate SI",
        command=calculate_si
    ).pack()
tk.Button(window, text="Simple Interest", command=open_si_window).pack()


def open_ci_window():
    third = tk.Toplevel(window)
    third.title("Compound Interest")
    tk.Label(third,text="CI Calculator").pack()
    third.geometry("400x300")
   #principal
    tk.Label(third,text="Principal").pack()
    principal_entry=tk.Entry(third)
    principal_entry.pack()
#rate
    tk.Label(third,text="Rate(%)").pack()
    rate_entry= tk.Entry(third)
    rate_entry.pack()
#time
    tk.Label(third,text="Time").pack()
    time_entry=tk.Entry(third)
    time_entry.pack() 
     # Result Label
    result_label = tk.Label(third, text="")
    result_label.pack()

    #calculateCI
    def calculate_CI():
        p=float(principal_entry.get())
        r=float(rate_entry.get())
        t=float(time_entry.get())
        ci=p*((1+r/100)**t)-p
        result_label.config(text=f"Compound Interest={ci}")
 #button
    tk.Button(third,text="Calculate CI ",command=calculate_CI).pack()
 
tk.Button(window,text="Compound Interst ",command=open_ci_window).pack()

window.mainloop()