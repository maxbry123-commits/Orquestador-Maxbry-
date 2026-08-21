"""🛷 REGALO DEL TRINEO — uoos_cli.py
Los 2 motores en UN comando, para cualquier proyecto:
  python regalos/uoos_cli.py parte1 documento.md [nombre_proyecto]
  python regalos/uoos_cli.py parte2 carpeta_codigo/ nombre_proyecto [destino]
Escribe el .md generado al lado y muestra el resumen. 0% LLM.
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from uoos.motor_tema_a import generar_uoos_parte1
from uoos.motor_tema_b import generar_uoos_parte2


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    modo, objetivo = argv[1], argv[2]
    if modo == "parte1":
        with open(objetivo, encoding="utf-8") as f:
            r = generar_uoos_parte1(f.read(),
                                    proyecto=argv[3] if len(argv) > 3 else None)
        salida = os.path.splitext(objetivo)[0] + "_UOOS1.md"
        with open(salida, "w", encoding="utf-8") as f:
            f.write(r["markdown"])
        print(json.dumps(r["uoos"]["manifest"], ensure_ascii=False, indent=2))
        print(f"🎁 escrito: {salida}")
        return 0
    if modo == "parte2":
        proyecto = argv[3] if len(argv) > 3 else "proyecto"
        destino = argv[4] if len(argv) > 4 else "github"
        r = generar_uoos_parte2(objetivo, proyecto, destino)
        salida = os.path.join(objetivo, f"UOOS2_{proyecto}.md")
        with open(salida, "w", encoding="utf-8") as f:
            f.write(r["markdown"])
        u = r["uoos2"]
        print(f"archivos={u['archivos']} tests={u['tests_detectados']} "
              f"lote={u['hash_lote'][:12]}")
        print(f"🎁 escrito: {salida}")
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
