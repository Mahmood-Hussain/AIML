# AI/ML Lecture Notes - LaTeX Project

> **An [EduCasheer](https://educasheer.in) Initiative**

Comprehensive LaTeX notes covering Lectures 1 through 10 of the Machine Learning and Deep Learning fundamentals course. Generated from lecture transcripts to provide textbook-style theoretical foundations and practical implementations from scratch.

## 👨‍🏫 Course Information

| | |
|---|---|
| **Instructor** | Musavir Khaliq |
| **Initiative** | EduCasheer |
| **Video Lectures** | [YouTube Playlist](https://youtube.com/playlist?list=PLG2XU_l-TcR8yWh4nKmPYMX5k9r-1XyBM) |

---

## 📦 Dependencies

### Windows
Install [MiKTeX](https://miktex.org/download) (recommended) or [TeX Live](https://tug.org/texlive/).

```powershell
# Using Chocolatey
choco install miktex

# Or using winget
winget install MiKTeX.MiKTeX
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install texlive-full
# Or minimal installation:
sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-science texlive-pictures
```

### macOS
```bash
brew install --cask mactex
# Or minimal:
brew install --cask basictex
```

---

## 🔨 Building the PDF

### Windows (PowerShell)
```powershell
cd latex
pdflatex main.tex
pdflatex main.tex  # Run twice for references
```

### Linux/macOS
```bash
cd latex
pdflatex main.tex
pdflatex main.tex  # Run twice for references
```

### Using latexmk (Recommended)
```bash
cd latex
latexmk -pdf main.tex
```

---

## 📁 Project Structure

```
AIMLNotes/
├── latex/
│   ├── main.tex          # Main document
│   ├── preamble.tex      # Packages & settings
│   └── chapters/         # Individual chapters
│       ├── lec01_introduction.tex
│       ├── lec02_supervised_learning.tex
│       ├── lec04_neurons.tex
│       ├── lec05_mlp.tex
│       ├── lec06_gradient_descent.tex
│       ├── lec07_universal_approximation.tex
│       ├── lec08_information_theory.tex
│       ├── lec09_backpropagation.tex
│       └── lec10_dl_systems.tex
├── transcripts/          # Source lecture transcripts (Lecture 1 to 10c)
└── README.md
```

---

## 📝 LaTeX Quick Reference

### Adding Images

```latex
\usepackage{graphicx}  % In preamble

% Basic image
\includegraphics[width=0.8\textwidth]{images/myimage.png}

% Image with caption
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.6\textwidth]{images/neural_network.png}
    \caption{A simple neural network architecture.}
    \label{fig:nn}
\end{figure}

% Reference: See Figure \ref{fig:nn}
```

**Placement options**: `h` (here), `t` (top), `b` (bottom), `p` (page), `!` (force)

---

### Creating Diagrams with TikZ

```latex
\usepackage{tikz}  % In preamble

% Simple neural network
\begin{tikzpicture}[
    node distance=2cm,
    neuron/.style={circle, draw, minimum size=1cm}
]
    % Input layer
    \node[neuron] (x1) at (0, 1) {$x_1$};
    \node[neuron] (x2) at (0, -1) {$x_2$};
    
    % Hidden layer
    \node[neuron] (h1) at (3, 0) {$h$};
    
    % Output
    \node[neuron] (y) at (6, 0) {$y$};
    
    % Connections
    \draw[->] (x1) -- (h1);
    \draw[->] (x2) -- (h1);
    \draw[->] (h1) -- (y);
\end{tikzpicture}
```

---

### Math Equations

```latex
% Inline math
The loss function $\mathcal{L} = \frac{1}{2}(y - \hat{y})^2$ measures error.

% Display math (numbered)
\begin{equation}
    \frac{\partial \mathcal{L}}{\partial w} = (y - \hat{y}) \cdot x
    \label{eq:gradient}
\end{equation}

% Display math (unnumbered)
\[
    \sigma(x) = \frac{1}{1 + e^{-x}}
\]

% Aligned equations
\begin{align}
    a^{(k)} &= W^{(k)} h^{(k-1)} + b^{(k)} \\
    h^{(k)} &= f(a^{(k)})
\end{align}
```

---

### Colored Boxes (using tcolorbox)

```latex
\usepackage{tcolorbox}  % In preamble

\begin{tcolorbox}[title={Key Concept}, colback=blue!5, colframe=blue!50]
    Backpropagation uses the chain rule to compute gradients efficiently.
\end{tcolorbox}
```

---

### Code Listings

```latex
\usepackage{listings}  % In preamble

\begin{lstlisting}[language=Python, caption={Sigmoid function}]
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
\end{lstlisting}
```

---

### Tables

```latex
\usepackage{booktabs}  % In preamble

\begin{table}[htbp]
    \centering
    \caption{Loss functions for different tasks}
    \begin{tabular}{lll}
        \toprule
        \textbf{Task} & \textbf{Distribution} & \textbf{Loss} \\
        \midrule
        Binary Classification & Bernoulli & BCE \\
        Multi-class & Categorical & CCE \\
        Regression & Gaussian & MSE \\
        \bottomrule
    \end{tabular}
\end{table}
```

---

### Useful Commands

| Command | Result |
|---------|--------|
| `\textbf{bold}` | **bold** |
| `\textit{italic}` | *italic* |
| `\texttt{code}` | `code` |
| `\mathbf{W}` | Bold math (matrix) |
| `\frac{a}{b}` | Fraction |
| `\sum_{i=1}^{n}` | Summation |
| `\partial` | Partial derivative symbol |
| `\nabla` | Gradient symbol |

---

## 🔧 Troubleshooting

**Missing packages**: MiKTeX auto-installs; for TeX Live run:
```bash
tlmgr install <package-name>
```

**References not showing**: Run `pdflatex` twice (or use `latexmk`).

**Font errors**: Install `texlive-fonts-extra` or use `lmodern` package.

---

## 📚 Resources

- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [TikZ Manual](https://tikz.dev/)
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [Detexify](http://detexify.kirelabs.org/) - Draw symbols to find LaTeX commands
