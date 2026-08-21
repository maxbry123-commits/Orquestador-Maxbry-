"""🎁 R6 — genera una app completa en 1 comando:
   python regalos/generar_app.py "app de gastos con login" ./mi_app"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generador.ensamblador import ensamblar_app
if __name__ == "__main__":
    idea = sys.argv[1] if len(sys.argv) > 1 else "app de notas"
    destino = sys.argv[2] if len(sys.argv) > 2 else "./app_generada"
    acta = ensamblar_app(idea, destino)
    print(json.dumps(acta, ensure_ascii=False, indent=2))
    sys.exit(0 if acta["ok"] else 1)
