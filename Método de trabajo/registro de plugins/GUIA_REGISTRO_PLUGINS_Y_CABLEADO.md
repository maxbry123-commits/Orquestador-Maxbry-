---
plugin_id: metodo-trabajo.registro-plugins.cableado
version: 1.0.0
type: method-guide
immutable_component: true
---
# Guía de registro de plugins y cableado

**crear → validar → registrar → dejar estable → conectar por plugin**.

Todo componente preparado para conexiones futuras debe dejar su plugin listo al crearse. Una vez validado/registrado, no se edita el archivo para conectarlo; se usan plugin, contrato, extension point, adapter o cable.

`REUSE > PATCH > ADAPT > GENERATE`. FAIL-CLOSED: sin source, contrato, tests o evidencia no hay PASS. No inventar APIs, rutas ni implementaciones. Código y documentos se registran según su tipo. Cambios incompatibles crean una nueva versión y conservan la anterior.

La arquitectura real del repositorio manda; Microkernel/Plugin Architecture es solo referencia, no una obligación de arquitectura.
