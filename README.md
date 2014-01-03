compressed_file_converter
=========================

Deascription: 
Convert many compressed files to .zip .tar .rar

Input File formates formats:
7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), TAR (.tar), XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo)

Output File formates :
zip(.zip), tar(.tar), rar(.rar)

dependencies :
sudo apt-get install unzip unrar p7zip-full lzop
Or
sudo apt-get install unzip unrar-free p7zip-full lzop

Python dependencies:
rarfile==2.6 (pip install rarfile==2.6)
pyunpack==0.0.3 (pip install pyunpack==0.0.3)
patool==0.17 (pip install http://downloads.sourceforge.net/project/patool/0.17/patool-0.17.tar.gz)
entrypoint2-0.0.6 (pip install entrypoint2==0.0.6)
argparse-1.2.1 (pip install argparse==1.2.1)
EasyProcess-0.1.6 (pip install EasyProcess==0.1.6)
