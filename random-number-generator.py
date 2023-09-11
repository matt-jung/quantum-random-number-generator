import tkinter as tk
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

window=tk.Tk()
window.title('Quantum Random Number Generator')


def generate_random_number():
    length=int(string_length_entry.get())

    qc=QuantumCircuit(length)
    qc.h(range(length))
    qc.measure_all()

    sim=AerSimulator()
    counts=sim.run(qc).result().get_counts()

    binary_string=max(counts,key=counts.get)

    random_number['text']=str(binary_string)

    
string_length_label=tk.Label(window,text='Enter string length:')
string_length_entry=tk.Entry(window,width=5)

generate_button=tk.Button(window,text='Generate!',command=generate_random_number)

random_number_label=tk.Label(window,text='Your randomly generated string:')
random_number=tk.Label(window,text='_')

string_length_label.grid(row=0,column=0,sticky='s')
string_length_entry.grid(row=1,column=0,sticky='n')
generate_button.grid(row=2,column=0,pady=10)
random_number_label.grid(row=3,column=0,sticky='s')
random_number.grid(row=4,column=0,sticky='n')

window.mainloop()