"""GENERADOR DE DESIGN SYSTEM — F1 parte 1 (gap más grande, Fase 04)
A partir de requisitos.json produce tokens de diseño completos:
colores (light+dark), tipografía, espaciado, radios — y los exporta
como tokens.json + variables.css listos para cualquier frontend.
100% determinista: el color base se deriva del hash del dominio,
así el mismo proyecto siempre recibe la misma identidad visual (L15).
"""
import json
import hashlib
import colorsys


def _hsl_a_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))


def generar_paleta(semilla: str) -> dict:
    """Color primario derivado del hash del dominio; el resto por armonía fija."""
    h = int(hashlib.sha256(semilla.encode()).hexdigest(), 16) % 360
    return {
        "primario":   _hsl_a_hex(h, 62, 46),
        "secundario": _hsl_a_hex((h + 30) % 360, 45, 55),
        "acento":     _hsl_a_hex((h + 180) % 360, 70, 50),
        "exito":      "#6FBF73",
        "error":      "#E0554F",
        "aviso":      "#D9A441",
        "light": {"fondo": "#FAFAF8", "superficie": "#FFFFFF",
                  "texto": "#1F1E1B", "texto_suave": "#5A5850", "borde": "#E2E0DA"},
        "dark":  {"fondo": "#17150F", "superficie": "#211F18",
                  "texto": "#E4DFD3", "texto_suave": "#A39E90", "borde": "#38352C"},
    }


def generar_tokens(requisitos: dict) -> dict:
    dominio = requisitos.get("proyecto", {}).get("dominio", "general")
    nombre = requisitos.get("proyecto", {}).get("nombre", "proyecto")
    return {
        "version": "1.0.0",
        "proyecto": nombre,
        "colores": generar_paleta(dominio),
        "tipografia": {
            "titulos": "Georgia, 'Times New Roman', serif",
            "cuerpo": "'Segoe UI', system-ui, sans-serif",
            "mono": "'IBM Plex Mono', 'Courier New', monospace",
            "escala": {"xs": "12px", "sm": "14px", "base": "16px",
                       "lg": "20px", "xl": "28px", "xxl": "40px"},
        },
        "espaciado": {"xs": "4px", "sm": "8px", "md": "16px",
                      "lg": "24px", "xl": "40px"},
        "radios": {"sm": "6px", "md": "10px", "lg": "16px", "pill": "999px"},
        "sombras": {"suave": "0 1px 3px rgba(0,0,0,.12)",
                    "media": "0 4px 12px rgba(0,0,0,.15)"},
    }


def exportar_css(tokens: dict) -> str:
    c, t = tokens["colores"], tokens["tipografia"]
    lineas = [":root {"]
    for k in ("primario", "secundario", "acento", "exito", "error", "aviso"):
        lineas.append(f"  --color-{k}: {c[k]};")
    for k, v in c["light"].items():
        lineas.append(f"  --{k.replace('_','-')}: {v};")
    for k, v in tokens["espaciado"].items():
        lineas.append(f"  --esp-{k}: {v};")
    for k, v in tokens["radios"].items():
        lineas.append(f"  --radio-{k}: {v};")
    lineas.append(f"  --fuente-titulos: {t['titulos']};")
    lineas.append(f"  --fuente-cuerpo: {t['cuerpo']};")
    lineas.append("}")
    lineas.append("[data-theme='dark'] {")
    for k, v in c["dark"].items():
        lineas.append(f"  --{k.replace('_','-')}: {v};")
    lineas.append("}")
    return "\n".join(lineas) + "\n"


def generar_y_guardar(requisitos: dict, carpeta: str) -> dict:
    import os
    os.makedirs(carpeta, exist_ok=True)
    tokens = generar_tokens(requisitos)
    with open(os.path.join(carpeta, "tokens.json"), "w", encoding="utf-8") as f:
        json.dump(tokens, f, ensure_ascii=False, indent=2, sort_keys=True)
    with open(os.path.join(carpeta, "variables.css"), "w", encoding="utf-8") as f:
        f.write(exportar_css(tokens))
    return tokens


if __name__ == "__main__":
    demo = generar_tokens({"proyecto": {"dominio": "recetas", "nombre": "proyecto_recetas"}})
    print(json.dumps(demo["colores"], indent=2)[:400])
