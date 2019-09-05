from flask import Flask, render_template, request
import os, datetime
from unipath import Path
app = Flask(__name__)

def ingresar(fecha, tiempo, tiempo2, temperatura, humedad):
  nombre=str(fecha)+'.csv'
  rt=Path(nombre)
  if f.exist():
      tr=open(nombre,'a')
      tr.write("\n"+str(tiempo2)+";"+str(tiempo)+";"+str(temperatura)+";"+str(humedad)+";")
      tr.close()
  else:
    tr=open(nombre,'a')
    tr.write("\nTiempo_Recibido;Tiempo_Dato;Temperatura;Humedad;")
    tr.write("\n"+str(tiempo2)+";"+str(tiempo)+";"+str(temperatura)+";"+str(humedad)+";")
    tr.close()


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/log')
def log():
  f=datetime.datetime.now()
  fecha=str(f.month)+str(f.day)+str(f.year)
  tiempo = request.args.get('tiempo') 
  temperatura= request.args.get('temperatura') 
  humedad= request.args.get('humedad')
  tiempo2=str(f.hour)+str(f.minute)
  ingresar(fecha, tiempo, tiempo2, temperatura, humedad)
  return 'Datos'

app.run()