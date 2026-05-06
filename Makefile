# ==========================================
# Makefile para Tesis (Portugués y Español)
# ==========================================

# Nombres de los archivos principales (sin la extensión .tex)
FILE_PT = tese
FILE_ES = tese_es

# Variables de entorno para buscar archivos en aux/
TEXINPUTS = ./aux//:
BSTINPUTS = ./aux//:

# Extensiones de archivos temporales a limpiar
CLEAN_EXTS = aux log toc out bbl blg lof lot run.xml synctex.gz dvi fdb_latexmk fls nav snm vrb

# .PHONY declara objetivos que no son archivos físicos
.PHONY: all pt es clean quick quick-es help

# 1. Regla por defecto: si escribes solo 'make', compila la versión en Portugués
all: pt

# 2. Compilación en Portugués (Default)
pt:
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_PT)
	BSTINPUTS=$(BSTINPUTS) bibtex $(FILE_PT)
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_PT)
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_PT)
	@echo "=============================================="
	@echo "--- Compilación en PORTUGUÉS (tese.pdf) OK ---"
	@echo "=============================================="

# 3. Compilación en Español
es:
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_ES)
	BSTINPUTS=$(BSTINPUTS) bibtex $(FILE_ES)
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_ES)
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_ES)
	@echo "=============================================="
	@echo "--- Compilación en ESPAÑOL (tese_es.pdf) OK --"
	@echo "=============================================="

# 4. Limpieza (Actualizado para incluir tex_es/)
clean:
	# Borrar temporales en la raíz
	rm -f $(foreach ext, $(CLEAN_EXTS), *.$(ext))
	# rm -f *.pdf
	# Borrar temporales en carpeta tex/ (Portugués)
	rm -f $(foreach ext, $(CLEAN_EXTS), tex/*.$(ext))
	# Borrar temporales en carpeta tex_es/ (Español)
	rm -f $(foreach ext, $(CLEAN_EXTS), tex_es/*.$(ext))
	# Borrar temporales en carpeta aux/
	rm -f $(foreach ext, $(CLEAN_EXTS), aux/*.$(ext))
	@echo "--- Todos los archivos temporales y PDFs han sido eliminados ---"

# ==========================================
# Compilación Rápida (Solo 1 pasada de PDF)
# ==========================================

# Rápido para Portugués (Default) > $ make quick
quick:
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_PT)
	@echo "--- PDF actualizado (Rápido - PT) ---"

# Rápido para Español             > $ make quick-es
quick-es:
	TEXINPUTS=$(TEXINPUTS) pdflatex $(FILE_ES)
	@echo "--- PDF actualizado (Rápido - ES) ---"

# ==========================================
# Ayuda rápida
# ==========================================
help:
	@echo "Opciones disponibles:"
	@echo "  make          -> Compila la versión en Portugués (tese.pdf)"
	@echo "  make pt       -> Lo mismo que arriba (Full: latex+bibtex+latex)"
	@echo "  make es       -> Compila la versión en Español (tese_es.pdf) (Full)"
	@echo "  make quick    -> Compila modificaciones leves en PT (1 pasada)"
	@echo "  make quick-es -> Compila modificaciones leves en ES (1 pasada)"
	@echo "  make clean    -> Borra temporales en raíz, tex/, tex_es/ y aux/"