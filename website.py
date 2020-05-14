import web
import os

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/download', 'download',
    '/download/(.*)', 'download',
    '/upload', 'upload',
    '/upload/', 'upload'
)

class index:
    def GET(self):
        return render.index()

class download:
    def GET(self, directory = ""):
        if "share/" != directory[:6]:
            directory = "share/" + directory
        listdirs = []
        listfiles = []
        if os.path.isdir(directory):
            if directory[-1] != '/':
                directory = directory + "/"
            for subdir in os.listdir(directory):
                if os.path.isdir(directory + subdir):
                    listdirs = listdirs + [subdir]
                else:
                    listfiles = listfiles + [subdir]
            return render.download(listdirs, listfiles, directory)
        elif os.path.isfile(directory):
            return open(directory).read()
        else:
            return "Error"

class upload:
    def GET(self):
        return render.upload("")
    def POST(self):
        x = web.input(myfile = {})
        filedir = "upload/"
        try:
            if 'myfile' in x:
                filepath=x.myfile.filename.replace('\\','/')
                if filepath == '':
                    raise Exception("file not found")
                filename=filepath.split('/')[-1]
                fout = open(filedir +'/'+ filename,'wb')
                fout.write(x.myfile.file.read())
                fout.close()
                return render.upload("success")
            else:
                raise Exception("file not found")
        except Exception as e:
            return render.upload("failed: " + str(e))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()