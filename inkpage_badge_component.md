# Inkpage Agency Badge Component (V2 - Premium)

Este componente foi desenhado para destacar a autoria digital de forma elegante e não-intrusiva, utilizando efeitos visuais premium para reforçar a percepção de qualidade da marca.

## 🛠️ Instalação

Copie e cole o código abaixo no rodapé (`<footer>`) ou na seção de créditos do seu projeto. 

**Dependências:** Tailwind CSS

```html
<!-- Inkpage Agency Badge -->
<a href="https://www.inkpage.com.br" target="_blank" rel="noopener"
  class="group relative flex items-center gap-3 px-4 py-2.5 rounded-xl bg-slate-50/50 hover:bg-white border border-slate-200/60 hover:border-purple-200/60 shadow-sm hover:shadow-lg hover:shadow-purple-100/50 transition-all duration-300 overflow-hidden">

  <!-- Visual Shine Effect -->
  <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/60 to-transparent -translate-x-full group-hover:translate-x-full duration-1000 transition-transform ease-in-out"></div>
  
  <div class="flex flex-col items-end relative z-10">
    <span
      class="text-[9px] font-extrabold text-slate-400 uppercase tracking-widest group-hover:text-purple-600 transition-colors duration-300">
      Presença Digital
    </span>
    <span class="font-display text-sm font-bold text-slate-700 group-hover:text-slate-900 leading-tight">
      Inkpage
    </span>
  </div>

  <div
    class="relative w-9 h-9 rounded-lg bg-slate-100 border border-slate-200/50 group-hover:border-purple-200 group-hover:bg-gradient-to-br group-hover:from-purple-600 group-hover:to-fuchsia-600 flex items-center justify-center transition-all duration-300 shadow-inner group-hover:shadow-lg z-10">
    <img src="public/images/logo-inkpage.svg" alt="Logo Inkpage"
      class="w-5 h-5 opacity-40 grayscale group-hover:grayscale-0 group-hover:opacity-100 group-hover:brightness-0 group-hover:invert transition-all duration-300">
  </div>
</a>
```

---

## ✨ Explicação do Efeito "Shine" (Shimmer)

O efeito visual de brilho que percorre o card ao passar o mouse é conhecido tecnicamente como **Shine Effect** ou **Shimmer Effect**. Ele simula o reflexo de luz em uma superfície polida (como vidro ou metal).

### Como funciona no código:

1.  **Elemento Fantasma (`div` absoluta):**
    Criamos uma `div` invisível que cobre toda a área do card (`absolute inset-0`), mas inicialmente posicionada fora da visão, à esquerda (`-translate-x-full`).

2.  **O Gradiente de Luz:**
    O fundo dessa div é um gradiente linear que vai de transparente p/ branco (60% opacidade) e volta para transparente. Isso cria a "faixa de luz".
    `bg-gradient-to-r from-transparent via-white/60 to-transparent`

3.  **A Animação (Hover):**
    Quando o usuário passa o mouse (`group-hover`), o navegador move essa div suavemente para a direita (`translate-x-full`), criando a ilusão de que um feixe de luz atravessou o card.
    
    A transição dura 1 segundo (`duration-1000`) e tem suavização na entrada e saída (`ease-in-out`), garantindo um movimento orgânico e sofisticado.

---

**© Inkpage | Presença Digital**
