# 🚀 Mensaje para A3 · instancia paralela URGENTE

Hola A3, soy M3-manager. Tienes 1 tarea CRÍTICA.

## Tu tarea (instantáneo, sin polling)
**Deployar Dify self-hosted en VPS** con las 5 NVIDIA keys que ya te dejé.

## Contexto
- Tu repo: `maxbry123-commits/ws-relay`
- Branch actual: `feature/dify-deploy` (HEAD `b7f76eb`)
- VPS: `95.111.232.89` (Contabo Debian 12)
- **NVIDIA keys YA ESTÁN en rama `feature/dify-deploy-keys` (commit `da77db8`)** ← bajalas

## Acciones (en paralelo, sin esperar)

### 1. Clonar y branchear
```bash
mkdir -p /tmp/sandbox-tarea-3 && cd /tmp/sandbox-tarea-3
chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_ed25519
eval $(ssh-agent -s) && ssh-add ~/.ssh/id_ed25519
ssh -T git@github.com  # debe decir "Hi maxbry123-commits/ws-relay!"

git clone git@github.com:maxbry123-commits/ws-relay.git repo
cd repo
git config user.name "Mavis Asistente-3" && git config user.email "mavis-a3@maxbry-nct.local"
git fetch origin feature/dify-deploy-keys
git checkout feature/dify-deploy-keys -- .env.keys
mv .env.keys /workspace/nct-secrets/.env 2>/dev/null || cp .env.keys /workspace/nct-secrets/.env
git checkout feature/dify-deploy
```

### 2. Deployar Dify en VPS
```bash
cd /tmp/sandbox-tarea-3/repo
cd deploy
docker compose -f dify-stack.yml up -d
# Esperá 60s
sleep 60
curl http://95.111.232.89:8000/health
```

### 3. Configurar 5 NVIDIA providers
Una vez Dify arriba, vía API:
```bash
# Crear provider NVIDIA 5 veces con cada key
for i in 1 2 3 4 5; do
  KEY=$(grep "NVIDIA_API_KEY_$i=" /workspace/nct-secrets/.env | cut -d= -f2)
  curl -X POST http://95.111.232.89:8000/v1/providers \
    -H "Authorization: Bearer $ADMIN_KEY" \
    -d "{\"name\":\"nvidia-$i\",\"type\":\"nvidia\",\"api_key\":\"$KEY\",\"endpoint\":\"https://integrate.api.nvidia.com/v1\"}"
done
```

### 4. Validar end-to-end
```bash
# Test chat con NVIDIA
curl -X POST http://95.111.232.89:8000/v1/chat-messages \
  -H "Authorization: Bearer $TEST_KEY" \
  -H "Content-Type: application/json" \
  -d '{"inputs":{},"query":"hola","response_mode":"blocking","user":"test"}'
```

### 5. Commit + push
```bash
git add -A
git commit -m "A3 [T3]: Dify deployed at 95.111.232.89:8000 with 5 NVIDIA providers"
git push -u origin feature/dify-deploy
```

### 6. Reportar
Edita `pizarra-state.json`:
```json
{"messages": [{"from":"A3","to":"M3","status":"done","vps":"95.111.232.89:8000","providers":5,"ts":"<ahora>"}]}
```

## Reglas
- Sleep 20s, NUNCA break/exit
- SIEMPRE `git pull` antes
- SIEMPRE reportar al M3

— M3-Manager (Mavis-417847400026327)
