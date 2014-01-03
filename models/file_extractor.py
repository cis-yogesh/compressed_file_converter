#importing python modules
import os
import re
import tarfile, zipfile
from datetime import datetime
# importing third party modules
from rarfile import RarFile
from pyunpack import Archive

# importing local modules
from . import EMAIL_REGEX, MD5_HASH, SHA1_HASH, CURRENT_PATH, file_stats,DELETE

#globle variables
DELETE=False



class ExtractAll():
    def __init__(self,filepath = None,extract_path = None):
        self.filepath = filepath
        self.extract_path = extract_path
    def executeall(self):
        self.filepath = self.set_filepath(self.filepath)
        file_extension = self.fileExtension(self.filepath)
        method = self.fileFormates(file_extension)
        if method:
            extract_folder_fullpath = method(self.filepath)
            self.WalkTreeAndExtract(extract_folder_fullpath)
        else:
            print "Unable to open given file"

    def fileExtension(self,file_name):
        match = re.compile(r"^.*[.](?P<ext>\w+)$",
          re.VERBOSE|re.IGNORECASE).match(file_name)
        if match:
            ext = match.group('ext')
            return ext
        else:
            return ''
    def readFilecontent(self,entry_file):
        with open(entry_file, "r") as f:
            currentfile = f.read()
            emails = re.findall(EMAIL_REGEX,currentfile)
            temp_dict = emails and {'email':[i[0] for i in emails if i]} or {'email':[]}
            md5hash = re.findall(MD5_HASH,currentfile)
            temp_dict['md5hash'] = md5hash and md5hash or []
            sha1hash = re.findall(SHA1_HASH,currentfile)
            temp_dict['sha1hash'] = sha1hash and sha1hash or []
            temp_dict['date'] = str(datetime.now())
            temp_dict['compressed_filename'] = self.filepath
            fileName, fileExtension = os.path.splitext(entry_file)
            temp_dict['filename'] = fileName
            temp_dict['fileformat'] = fileExtension
            print entry_file
            #temp_dict['file_size']  = os.path.getsize(entry_file)
            if emails or md5hash or sha1hash:
                file_stats.append(temp_dict)

    def extract_tar(self,tarfile_fullpath, delete_tar_file=DELETE,Path=True):
        tarfile_name = os.path.basename(tarfile_fullpath)
        parent_dir = os.path.dirname(tarfile_fullpath)
        extract_folder_name = tarfile_name[:-1*len(self.fileExtension(tarfile_name))-1]
        if Path:
            if self.extract_path:
                extract_folder_fullpath = os.path.join(self.extract_path, extract_folder_name)
            else:
                extract_folder_fullpath = os.path.join(parent_dir,"archivedFiles", extract_folder_name)
        else:
            extract_folder_fullpath = os.path.join(parent_dir, extract_folder_name)
        
        try:
            tar = tarfile.open(tarfile_fullpath)
            tar.extractall(extract_folder_fullpath)
            tar.close()
            if delete_tar_file:
                os.remove(tarfile_fullpath)
            return extract_folder_fullpath
        except Exception as e:
            # Exceptions can occur while opening a damaged tar file.
            print 'Error occured while extracting %s\n'\
            'Reason: %s' %(tarfile_fullpath, e)
            return

    def extract_zip(self,tarfile_fullpath, delete_tar_file=DELETE,Path=True):
        tarfile_name = os.path.basename(tarfile_fullpath)
        parent_dir = os.path.dirname(tarfile_fullpath)
        extract_folder_name = tarfile_name[:-1*len(self.fileExtension(tarfile_name))-1]
        if Path:
            if self.extract_path:
                extract_folder_fullpath = os.path.join(self.extract_path, extract_folder_name)
            else:
                extract_folder_fullpath = os.path.join(parent_dir,"archivedFiles", extract_folder_name)
        else:
            extract_folder_fullpath = os.path.join(parent_dir, extract_folder_name)
        
        try:
            zip = zipfile.ZipFile(tarfile_fullpath, "r")
            zip.extractall(extract_folder_fullpath)
            zip.close()
            if delete_tar_file:
                os.remove(tarfile_fullpath)
            return extract_folder_fullpath
        except Exception as e:
            # Exceptions can occur while opening a damaged tar file.
            print 'Error occured while extracting %s\n'\
            'Reason: %s' %(tarfile_fullpath, e)
            return

    def extract_rar(self,tarfile_fullpath, delete_tar_file=DELETE,Path=True):
        tarfile_name = os.path.basename(tarfile_fullpath)
        parent_dir = os.path.dirname(tarfile_fullpath)
        extract_folder_name = tarfile_name[:-1*len(self.fileExtension(tarfile_name))-1]
        if Path:
            if self.extract_path:
                extract_folder_fullpath = os.path.join(self.extract_path, extract_folder_name)
            else:
                extract_folder_fullpath = os.path.join(parent_dir,"archivedFiles", extract_folder_name)
        else:
            extract_folder_fullpath = os.path.join(parent_dir, extract_folder_name)
        
        try:
            rar = RarFile(tarfile_fullpath, "r")
            rar.extractall(extract_folder_fullpath)
            rar.close()
            if delete_tar_file:
                os.remove(tarfile_fullpath)
            return extract_folder_fullpath
        except Exception as e:
            # Exceptions can occur while opening a damaged tar file.
            print 'Error occured while extracting %s\n'\
            'Reason: %s' %(tarfile_fullpath, e)
            return

    def extract_7z(self,tarfile_fullpath, delete_tar_file=DELETE,Path=True):
        tarfile_name = os.path.basename(tarfile_fullpath)
        parent_dir = os.path.dirname(tarfile_fullpath)
        extract_folder_name = tarfile_name[:-1*len(self.fileExtension(tarfile_name))-1]
        if Path:
            if self.extract_path:
                extract_folder_fullpath = os.path.join(self.extract_path, extract_folder_name)
            else:
                extract_folder_fullpath = os.path.join(parent_dir,"archivedFiles", extract_folder_name)
        else:
            extract_folder_fullpath = os.path.join(parent_dir, extract_folder_name)
        
        try:
            if not os.path.exists(extract_folder_fullpath):
                os.makedirs(extract_folder_fullpath)
            Archive(tarfile_fullpath).extractall(extract_folder_fullpath)
            #z7.extractall(extract_folder_fullpath)
            if delete_tar_file:
                os.remove(tarfile_fullpath)
            return extract_folder_fullpath
        except Exception as e:
            # Exceptions can occur while opening a damaged tar file.
            print 'Error occured while extracting %s\n'\
            'Reason: %s' %(tarfile_fullpath, e)
            return


    def WalkTreeAndExtract(self,parent_dir):
        try:
            dir_contents = os.listdir(parent_dir)
        except OSError as e:
            print 'Error occured. Could not open folder %s\n'\
            'Reason: %s' %(parent_dir, e)
            return
        for content in dir_contents:
            content_fullpath = os.path.join(parent_dir, content)
            if os.path.isdir(content_fullpath):
                # If content is a folder, walk it down completely.
                self.WalkTreeAndExtract(content_fullpath)
            elif os.path.isfile(content_fullpath):
                file_extension = self.fileExtension(content_fullpath)
                method = self.fileFormates(file_extension)
                if method:
                    extract_folder_name = method(content_fullpath,Path=False)
                    if extract_folder_name:
                        dir_contents.append(extract_folder_name)
            else:
                print 'Skipping %s. <Neither file nor folder>' % content_fullpath


    def set_filepath(self,file_path):
        if '/' in file_path:
            pass
        else:
            file_path = os.path.join(CURRENT_PATH,file_path)
        import platform
        if platform.system() == "Linux":
            return file_path.replace("\\","/")
        elif platform.system() == "Linux":
            return file_path.replace("/","\\")
        else:
            return file_path
    def fileFormates(self,file_extension):
        FILE_TYPE_DICT = { 
                    'zip': self.extract_zip,
                    'zpi':self.extract_zip,
                    'zipx': self.extract_zip,
                    'tar': self.extract_tar,
                    'tgz': self.extract_tar,
                    #'tgz': self.extract_tar,
                    'rar': self.extract_rar,
                    #start of 7z methods,
                    '7z' : self.extract_7z,
                    'ace' :self.extract_7z,
                    'alz': self.extract_7z,
                    'arc': self.extract_7z,
                    'arj':self.extract_7z,
                    'bz2':self.extract_7z,
                    'z':self.extract_7z,
                    'deb':self.extract_7z,
                    'gz':self.extract_7z,
                    'gzip':self.extract_7z,
                    'lha':self.extract_7z,
                    'lzh':self.extract_7z,
                    'lz':self.extract_7z,
                    'lzma':self.extract_7z,
                    'lzo':self.extract_7z,
                    'rpm':self.extract_7z,
                    'rz':self.extract_7z,
                    'xz':self.extract_7z,
                    'jar':self.extract_7z,
                    'zoo':self.extract_7z,
                    'a':self.extract_7z,
                    'ar':self.extract_7z,
                    #end of 7z methods,

                    #'rar5': self.extract_rar,
                    #'r00': self.extract_rar,
                    #'.gzip':self.extract_all_gzip, 
                }
        if file_extension in FILE_TYPE_DICT.keys():
            return FILE_TYPE_DICT[file_extension]
        else:
            return None




class AchieveAll():
    def __init__(self,filename = None):
        self.filename = filename

    def executeall(self):
        #import pdb; pdb.set_trace()
        file_extension = self.fileExtension(self.filename)
        method = self.fileFormates(file_extension)
        if method:
            extract_folder_fullpath = method(self.filename)
        else:
            print "Unable to open given file"

    def fileExtension(self,file_name):
        match = re.compile(r"^.*[.](?P<ext>\w+)$",
          re.VERBOSE|re.IGNORECASE).match(file_name)
        if match:
            ext = match.group('ext')
            return ext
        else:
            return ''
    def zipdir(self,path, zip):
        for root, dirs, files in os.walk(path):
            for file in files:
                zip.write(os.path.join(root, file))
                

    def achieve_zip(self,filename):
        zipf = zipfile.ZipFile(filename, 'w')
        self.zipdir('archivedFiles/', zipf)
        zipf.close()

    def fileFormates(self,file_extension):
        FILE_TYPE_DICT = { 
                    'zip': self.achieve_zip,
                }
        if file_extension in FILE_TYPE_DICT.keys():
            return FILE_TYPE_DICT[file_extension]
        else:
            return None