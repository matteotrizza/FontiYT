# Server AI in casa - comandi

Ollama esposto sulla rete di casa, piu' Open WebUI come interfaccia.
Porte usate: **11434** (Ollama) e **3000** (Open WebUI).

---

## Windows

PowerShell **come amministratore**.

### 1. Dire a Ollama di ascoltare tutta la rete

```powershell
[Environment]::SetEnvironmentVariable('OLLAMA_HOST','0.0.0.0','Machine')
[Environment]::SetEnvironmentVariable('OLLAMA_KEEP_ALIVE','-1','Machine')
```

`OLLAMA_HOST` apre Ollama alle richieste che arrivano dagli altri dispositivi.
`OLLAMA_KEEP_ALIVE` a `-1` tiene il modello in memoria video: senza, dopo qualche minuto viene scaricato e ogni domanda lo fa ricaricare da capo.

### 2. Riavviare Ollama

Chiudilo dalla barra delle applicazioni (freccia per le icone nascoste, tasto destro, esci) e riavvialo.

### 3. Verificare che stia ascoltando

```powershell
netstat -ano | findstr 11434
```

Deve comparire una riga con `TCP  0.0.0.0:11434`. Se compare `127.0.0.1:11434` la variabile non ha avuto effetto: controlla di aver riavviato Ollama.

### 4. Aprire le porte nel firewall

```powershell
New-NetFirewallRule -DisplayName "Ollama" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "Open WebUI" -Direction Inbound -LocalPort 3000 -Protocol TCP -Action Allow
```

### 5. Docker Desktop e WSL

Verifica prima che la virtualizzazione sia attiva: Gestione attivita', Prestazioni, CPU, voce Virtualizzazione. Se e' disattivata si abilita dal BIOS.

Se Docker chiede WSL:

```powershell
wsl --install
```

**Riavvia il computer** prima di avviare Docker: l'installazione di WSL richiede il riavvio per caricare driver e servizi di virtualizzazione.

### 6. Installare Open WebUI

```powershell
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Poi apri `http://localhost:3000`.
**Il primo account che registri e' quello di amministratore**, quindi segnati la password.

---

## macOS

Terminale.

### 1. Dire a Ollama di ascoltare tutta la rete

```bash
launchctl setenv OLLAMA_HOST "0.0.0.0"
launchctl setenv OLLAMA_KEEP_ALIVE "-1"
```

### 2. Riavviare Ollama

Esci da Ollama dalla barra dei menu in alto e riaprilo.

### 3. Verificare che stia ascoltando

```bash
lsof -iTCP:11434 -sTCP:LISTEN
```

### 4. Firewall

Su macOS il firewall e' disattivato di default e non serve fare niente. Se lo hai acceso, autorizza Ollama quando il sistema lo chiede.

### 5. Installare Open WebUI

Stesso comando di Windows, con Docker Desktop per Mac installato:

```bash
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Attenzione: le variabili non sopravvivono al riavvio

`launchctl setenv` vale solo per la sessione corrente. Per renderle permanenti serve un LaunchAgent, cioe' un file `~/Library/LaunchAgents/com.ollama.env.plist` con dentro le due variabili, caricato con `launchctl load`.
