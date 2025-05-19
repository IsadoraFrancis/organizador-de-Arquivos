# 🗂️ Organizador de Arquivos

Um projeto simples de automação em Python que organiza automaticamente os arquivos de uma pasta com base no **tipo de arquivo** (extensão), movendo-os para subpastas específicas como: `imagens`, `pdfs`, `csv`, e `planilhas`.

---

## 💡 Funcionalidades

- Organiza arquivos com base em sua **extensão**.
- Move arquivos para pastas como:
  - 📸 `imagens` (`.png`, `.jpg`, `.jpeg`)
  - 📊 `planilhas` (`.xlsx`)
  - 📄 `pdfs` (`.pdf`)
  - 📈 `csv` (`.csv`)
- Cria as subpastas automaticamente, se não existirem.
- Interface interativa para o usuário selecionar a pasta.

---

## 🧪 Tecnologias utilizadas

- Python 3
- Biblioteca `tkinter`

---

## ▶️ Como usar

1. Clone este repositório ou copie o script:

   ```
   git clone https://github.com/IsadoraFrancis/organizador-de-Arquivos.git
   
   ```
2. Execute o script Python:
```

python main.py

```
3. Escolha a pasta que deseja organizar através da janela que será exibida.

4. Pronto! Os arquivos serão movidos para suas respectivas subpastas.

---
## 📁 Exemplo de organização

Antes:
```
/Downloads
├── imagem.png
├── relatorio.pdf
├── dados.csv
```
Depois:
```
/Downloads
├── imagens
│   └── imagem.png
├── pdfs
│   └── relatorio.pdf
├── csv
│   └── dados.csv
```
## 🙌 Créditos
Este projeto foi desenvolvido como prática de automação com Python, focando em interação com o sistema de arquivos e interface gráfica com tkinter.
