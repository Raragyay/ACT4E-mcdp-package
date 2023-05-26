
all:

base_url=https://z7-stage-editor-local.zuper.ai/editor/gh/co-design-models/ACT4E-exercises-spring2023/main/view
#download=wget -r -l 0 -np -A '.*repr1.*,.*mcdpr1.*' --content-disposition -nd -P downloaded
download=wget   -r -l 0 -np  --content-disposition -nd -P downloaded #--load-cookies cookies.txt

download:
	#rm -f downloaded/*
	#wget --save-cookies cookies.txt --keep-session-cookies $(base_url)/
	$(download) "$(base_url)/libraries/lib1-simple/"
	$(download) "$(base_url)/libraries/lib1-parts/"

	rm -f  downloaded/index*
