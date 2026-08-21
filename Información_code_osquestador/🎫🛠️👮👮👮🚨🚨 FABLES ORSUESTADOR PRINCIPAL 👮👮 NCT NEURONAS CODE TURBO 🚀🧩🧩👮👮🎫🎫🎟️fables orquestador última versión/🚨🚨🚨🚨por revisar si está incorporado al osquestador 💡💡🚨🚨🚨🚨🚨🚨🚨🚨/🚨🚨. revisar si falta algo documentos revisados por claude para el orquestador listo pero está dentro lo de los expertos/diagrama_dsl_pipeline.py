# ═══════════════════════════════════════════════════════
# DIAGRAMA DSL — DAG DEL PIPELINE MAXBRY_JARVIS v4.0
# FORMATO: NODOS + ARISTAS + CONDICIONES DE FLUJO
# ═══════════════════════════════════════════════════════

from dataclasses import dataclass, field
from typing import List, Optional, Dict
from enum import Enum

# ──────────────────────────────────────────────────────
# DEFINICIÓN DEL DSL
# ──────────────────────────────────────────────────────

class NodeType(Enum):
    INICIO = "INICIO"
    ESTADO = "ESTADO"
    RECEPCION = "RECEPCION"
    CLASIFICACION = "CLASIFICACION"
    INVESTIGACION = "INVESTIGACION"
    COUNCIL = "COUNCIL"
    EXTRACCION = "EXTRACCION"
    CONVERSION = "CONVERSION"
    PROPUESTAS = "PROPUESTAS"
    PLANIFICACION = "PLANIFICACION"
    ANALISIS_RIESGOS = "ANALISIS_RIESGOS"
    EJECUCION = "EJECUCION"
    REVISION = "REVISION"
    AUDITORIA = "AUDITORIA"
    FIREWALL = "FIREWALL"
    ENTREGA = "ENTREGA"
    PARCHE = "PARCHE"
    FIN = "FIN"
    DECISION = "DECISION"  # Nodo condicional
    LOOP = "LOOP"          # Nodo de retroalimentación

@dataclass
class Node:
    id: str
    nombre: str
    tipo: NodeType
    agentes: List[str] = field(default_factory=list)
    descripcion: str = ""
    
@dataclass
class Edge:
    desde: str
    hacia: str
    condicion: str = "SIEMPRE"  # SIEMPRE, OK, RECHAZADO, SCORE>=70, etc.
    
@dataclass
class DAG:
    nombre: str
    version: str
    nodos: List[Node] = field(default_factory=list)
    aristas: List[Edge] = field(default_factory=list)
    
    def agregar_nodo(self, nodo: Node):
        self.nodos.append(nodo)
        
    def agregar_arista(self, desde: str, hacia: str, condicion: str = "SIEMPRE"):
        self.aristas.append(Edge(desde, hacia, condicion))
        
    def render(self) -> str:
        """Renderiza el DAG en formato texto visual"""
        output = []
        output.append(f"╔═══════════════════════════════════════════════════════╗")
        output.append(f"║  DAG: {self.nombre}")
        output.append(f"║  VERSIÓN: {self.version}")
        output.append(f"║  NODOS: {len(self.nodos)} | ARISTAS: {len(self.aristas)}")
        output.append(f"╚═══════════════════════════════════════════════════════╝")
        output.append("")
        
        # Agrupar nodos por nivel
        niveles = self._calcular_niveles()
        
        for nivel, nodos_nivel in enumerate(niveles):
            output.append(f"┌─── NIVEL {nivel} ───┐")
            for nodo_id in nodos_nivel:
                nodo = next(n for n in self.nodos if n.id == nodo_id)
                agentes_str = f" [{', '.join(nodo.agentes)}]" if nodo.agentes else ""
                output.append(f"│ [{nodo.id}] {nodo.nombre}{agentes_str}")
                output.append(f"│    └─ {nodo.descripcion}")
            output.append("└" + "─" * 20)
            output.append("        │")
            output.append("        ▼")
        
        # Mostrar aristas con condiciones
        output.append("┌─── FLUJOS CONDICIONALES ───┐")
        for arista in self.aristas:
            if arista.condicion != "SIEMPRE":
                output.append(f"│ {arista.desde} ──[{arista.condicion}]──► {arista.hacia}")
        output.append("└" + "─" * 30)
        
        return "\n".join(output)
    
    def _calcular_niveles(self) -> List[List[str]]:
        """Calcula los niveles del DAG para renderizado"""
        niveles = []
        visitados = set()
        nivel_actual = ["STEP-00"]
        
        while nivel_actual:
            niveles.append(nivel_actual)
            visitados.update(nivel_actual)
            siguiente_nivel = []
            for arista in self.aristas:
                if arista.desde in nivel_actual and arista.hacia not in visitados:
                    if arista.hacia not in siguiente_nivel:
                        siguiente_nivel.append(arista.hacia)
            nivel_actual = siguiente_nivel
        
        return niveles
    
    def exportar_mermaid(self) -> str:
        """Exporta el DAG a formato Mermaid para visualización"""
        output = ["```mermaid", "graph TD"]
        
        for nodo in self.nodos:
            shape = self._obtener_forma_mermaid(nodo.tipo)
            label = f"{nodo.id}<br/>{nodo.nombre}"
            output.append(f'    {nodo.id}{shape["inicio"]}"{label}"{shape["fin"]}')
        
        output.append("")
        for arista in self.aristas:
            arrow = f"-->|{arista.condicion}|" if arista.condicion != "SIEMPRE" else "-->"
            output.append(f"    {arista.desde} {arrow} {arista.hacia}")
        
        output.append("```")
        return "\n".join(output)
    
    def _obtener_forma_mermaid(self, tipo: NodeType) -> Dict[str, str]:
        """Define la forma visual según el tipo de nodo"""
        formas = {
            NodeType.INICIO: {"inicio": "((", "fin": "))"},
            NodeType.FIN: {"inicio": "((", "fin": "))"},
            NodeType.DECISION: {"inicio": "{", "fin": "}"},
            NodeType.LOOP: {"inicio": "[/", "fin": "/]"},
        }
        return formas.get(tipo, {"inicio": "[", "fin": "]"})


# ──────────────────────────────────────────────────────
# CONSTRUCCIÓN DEL DAG DEL PIPELINE
# ──────────────────────────────────────────────────────

def construir_dag_pipeline() -> DAG:
    """Construye el DAG completo del pipeline MAXBRY_JARVIS v4.0"""
    
    dag = DAG(
        nombre="MAXBRY_JARVIS_ENGINE v4.0 — PIPELINE ESTRUCTURADO",
        version="PIPELINE-v4.0"
    )
    
    # ── DEFINICIÓN DE NODOS ──
    
    dag.agregar_nodo(Node(
        id="STEP-00",
        nombre="PANEL_DE_ESTADO",
        tipo=NodeType.ESTADO,
        descripcion="Recuperar y mostrar estado al inicio de sesión"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-01",
        nombre="RECEPCIÓN_Y_CLARIFICACIÓN",
        tipo=NodeType.RECEPCION,
        agentes=["ROL-3-ESPECIALISTA", "ROL-1-ANALISTA"],
        descripcion="Leer input completo, identificar gaps, preguntar máx 3"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-02",
        nombre="CLASIFICACIÓN_Y_ENRUTAMIENTO",
        tipo=NodeType.CLASIFICACION,
        agentes=["CLASSIFIER"],
        descripcion="Detectar tipo + complejidad + urgencia + ruta"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-03",
        nombre="INVESTIGACIÓN_OBLIGATORIA",
        tipo=NodeType.INVESTIGACION,
        agentes=["INVESTIGATOR"],
        descripcion="Buscar antes de crear: internet, YouTube, modelos OS"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-04",
        nombre="COUNCIL_MULTI_ROL",
        tipo=NodeType.COUNCIL,
        agentes=["ROL-1", "ROL-2", "ROL-3", "ROL-4", "ROL-5", "ANALYST", "HISTORIAN", "IMPROVER"],
        descripcion="Activar 5 roles internos + agentes de apoyo"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-05",
        nombre="EXTRACCIÓN_DE_IDEAS",
        tipo=NodeType.EXTRACCION,
        agentes=["ROL-1-ANALISTA"],
        descripcion="Extraer ideas unitarias sin interpretación"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-06",
        nombre="CONVERSIÓN_TÉCNICA",
        tipo=NodeType.CONVERSION,
        agentes=["ROL-2-INGENIERO"],
        descripcion="Convertir cada idea → formato 4 bloques técnicos"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-07",
        nombre="PROPUESTAS_PREVIAS",
        tipo=NodeType.PROPUESTAS,
        agentes=["PLANNER", "ARCHITECT"],
        descripcion="Presentar 2-3 opciones antes de construir"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-08",
        nombre="PLANIFICACIÓN_Y_ARQUITECTURA",
        tipo=NodeType.PLANIFICACION,
        agentes=["PLANNER", "ARCHITECT"],
        descripcion="Diseñar estructura + interfaces + dependency_map"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-09",
        nombre="ANÁLISIS_DE_RIESGOS",
        tipo=NodeType.ANALISIS_RIESGOS,
        agentes=["ANALYST"],
        descripcion="Failure analysis + edge cases + riesgos críticos"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-10",
        nombre="EJECUCIÓN_CONTROLADA",
        tipo=NodeType.EJECUCION,
        agentes=["EXECUTOR"],
        descripcion="Generar contenido estructurado por bloques máx 40 líneas"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-11",
        nombre="REVISIÓN_Y_AUTO_CORRECCIÓN",
        tipo=NodeType.REVISION,
        agentes=["REVIEWER"],
        descripcion="Validar + asignar confianza 0-100"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-12",
        nombre="AUDITORÍA_PRECIERRE",
        tipo=NodeType.AUDITORIA,
        agentes=["ROL-4-AUDITOR"],
        descripcion="Verificar integridad + emitir parche de gaps"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-13",
        nombre="FIREWALL_FINAL",
        tipo=NodeType.FIREWALL,
        agentes=["FIREWALL"],
        descripcion="Último filtro: alucinaciones, formato, leyes"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-14",
        nombre="ENTREGA_FINAL_Y_MEMORIA",
        tipo=NodeType.ENTREGA,
        agentes=["HISTORIAN", "IMPROVER"],
        descripcion="Entregar + registrar en memory_log + aprender"
    ))
    
    dag.agregar_nodo(Node(
        id="STEP-15",
        nombre="PARCHE_DE_CIERRE",
        tipo=NodeType.PARCHE,
        descripcion="Generar parche reutilizable + versioning"
    ))
    
    # ── DEFINICIÓN DE ARISTAS (FLUJOS) ──
    
    # Flujo principal (secuencial)
    dag.agregar_arista("STEP-00", "STEP-01")
    dag.agregar_arista("STEP-01", "STEP-02", "DATOS_SUFICIENTES")
    dag.agregar_arista("STEP-01", "STEP-01", "FALTAN_DATOS → PREGUNTAR_3")
    dag.agregar_arista("STEP-02", "STEP-03")
    dag.agregar_arista("STEP-03", "STEP-04", "REPORTE_APROBADO")
    dag.agregar_arista("STEP-03", "STEP-03", "REPORTE_VACÍO → REINVESTIGAR")
    dag.agregar_arista("STEP-04", "STEP-05", "COUNCIL_OK")
    dag.agregar_arista("STEP-04", "STEP-01", "CONTRADICCIÓN → FREEZE")
    dag.agregar_arista("STEP-05", "STEP-06")
    dag.agregar_arista("STEP-06", "STEP-07", "CONVERSIÓN_OK")
    dag.agregar_arista("STEP-06", "STEP-04", "CONTRADICCIÓN → ESCALAR")
    dag.agregar_arista("STEP-07", "STEP-08", "PROPUESTA_APROBADA")
    dag.agregar_arista("STEP-08", "STEP-09", "ESTRUCTURA_OK")
    dag.agregar_arista("STEP-09", "STEP-10", "RIESGOS_DOCUMENTADOS")
    dag.agregar_arista("STEP-09", "STEP-08", "RIESGO_CRÍTICO → REPLANIFICAR")
    dag.agregar_arista("STEP-10", "STEP-11")
    dag.agregar_arista("STEP-11", "STEP-12", "CONFIANZA>=70")
    dag.agregar_arista("STEP-11", "STEP-10", "CONFIANZA<70 → REINYECTAR")
    dag.agregar_arista("STEP-12", "STEP-13", "SIN_GAPS")
    dag.agregar_arista("STEP-12", "STEP-10", "CON_GAPS → PARCHE")
    dag.agregar_arista("STEP-13", "STEP-14", "LIMPIO + SCORE>=70")
    dag.agregar_arista("STEP-13", "STEP-10", "FALLA → REINYECTAR")
    dag.agregar_arista("STEP-14", "STEP-15")
    
    return dag


# ──────────────────────────────────────────────────────
# EJECUCIÓN DEL EJEMPLO
# ──────────────────────────────────────────────────────

if __name__ == "__main__":
    dag = construir_dag_pipeline()
    
    # Mostrar representación textual
    print(dag.render())
    print("\n" + "="*60 + "\n")
    
    # Mostrar formato Mermaid (para visualizar en Markdown/GitHub)
    print("FORMATO MERMAID (para visualizar):")
    print(dag.exportar_mermaid())
    
    # Guardar también en archivo separado
    with open("/workspace/diagrama_mermaid.md", "w") as f:
        f.write("# DAG del Pipeline MAXBRY_JARVIS v4.0\n\n")
        f.write(dag.exportar_mermaid())
        f.write("\n\n## Descripción\n\n")
        f.write("Este diagrama muestra el flujo del pipeline con sus 16 nodos principales y las condiciones de bifurcación entre ellos.")