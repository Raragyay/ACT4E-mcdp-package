
all:

base_url=https://z7-stage-editor-local.zuper.ai/editor/gh/co-design-models/ACT4E-exercises-spring2023/main/view
download=wget -r -l 0 -np  --content-disposition -nd -P downloaded

download:
	rm -f downloaded/*
	$(download) "$(base_url)/libraries/lib1-simple/"
	$(download) "$(base_url)/libraries/lib1-parts/"

	rm -f  downloaded/index*
