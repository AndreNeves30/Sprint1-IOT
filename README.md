# 👁️ Sistema de Detecção de Piscar de Olhos e Abertura de Boca  
### Utilizando OpenCV + MediaPipe (FaceMesh)

## 📌 Objetivo
Este projeto implementa uma aplicação local capaz de **detectar ações faciais** de **piscadas** e **abertura da boca** usando **OpenCV** e **MediaPipe FaceMesh**.
---

## 🚀 Tecnologias Utilizadas

- **Python**
- **OpenCV**
- **MediaPipe FaceMesh**
- **Comunicação Serial**
---

## 🧠 Como Funciona?

### 1. **Detecção Facial**
O MediaPipe FaceMesh identifica 468 pontos (landmarks) no rosto.

### 2. **Cálculo do EAR — Eye Aspect Ratio**
Usado para detectar **piscadas**:

EAR = (v1 + v2) / (2 * h)
Valores abaixo do limiar → olho fechado  
Valores acima → olho aberto

### 3. **Cálculo do MAR — Mouth Aspect Ratio**
Usado para detectar **quando a boca abre**:
MAR = distancia_vertical / distancia_horizontal
Quando MAR > limiar → boca aberta.
### 4. **Histerese**
Evita falsos positivos criando "zonas":  
- Um limite para ativar  
- Um limite diferente para desativar  

Isso estabiliza muito a detecção.

---

## 🎛️ Parâmetros Ajustáveis (e seus impactos)

| Parâmetro | Descrição | Impacto |
|----------|-----------|---------|
| `LIMIAR_FECHAR` | EAR mínimo para considerar olho fechado | Muito alto → não detecta piscar / Muito baixo → falso-positivo |
| `LIMIAR_ABRIR` | EAR para voltar ao estado aberto | Evita ficar alternando rapidamente |
| `LIMIAR_MAR_ABRIR` | MAR para boca aberta | Valores maiores tornam a detecção mais rígida |
| `LIMIAR_MAR_FECHAR` | MAR para boca fechada | Histerese de estabilidade |
| `frames_fechado` | Quantos frames confirmar antes de contar piscar | Evita falsos positivos |

Durante o vídeo, esses valores podem ser mostrados na tela para demonstrar o efeito em tempo real.

---

## ▶️ Execução

### 1. Instale dependências:

pip install opencv-python mediapipe pyserial

---

## Nota Ética sobre Uso de Dados Faciais

Este projeto utiliza técnicas de visão computacional para detectar movimentos faciais (piscadas e abertura de boca) **sem realizar identificação de pessoas** e **sem armazenar nenhuma imagem, vídeo ou dado biométrico**.

Todas as operações são feitas **localmente**, diretamente no dispositivo do usuário.

### Princípios adotados:

- **Privacidade primeiro:**  
  Nenhuma informação facial é enviada para servidores externos ou armazenada.

- **Transparência:**  
  O código é aberto e permite que qualquer pessoa veja exatamente como o processamento é feito.

- **Uso responsável:**  
  O sistema deve ser utilizado exclusivamente para fins educacionais, acadêmicos ou prototipação técnica.

- **Não discriminação:**  
  O modelo não foi treinado por mim, mas sim utiliza frameworks externos. Ainda assim, todo uso deve respeitar a diversidade de rostos, tons de pele e características faciais.

- **Consentimento:**  
  Qualquer usuário filmado deve ter ciência de que há uma câmera em funcionamento.

### Limitações éticas:

- Detecções automatizadas podem apresentar vieses de iluminação, oclusão ou ângulos.
- O sistema **não substitui sistemas de segurança real**.
- Não deve ser usado para vigilância, monitoramento não consentido ou qualquer atividade que viole a privacidade.

Ao utilizar este projeto, o usuário concorda em respeitar esses princípios e adotar práticas responsáveis de uso de visão computacional.

##🧑‍💻 Grupo

O projeto foi desenvolvido pela seguinte equipe:

| Nome | RM |
| :--- | :--- |
| André Neves | [RM 553515] |
| Beatriz Dantas | [RM 554044] |
| Caio Tominaga | [RM 553633] |
| Eduardo Brites | [RM 552943] |
| Isabela Barcellos | [RM 553746] |
| Thaís Leoncio | [RM 553892] |   
   
   
