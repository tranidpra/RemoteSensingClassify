import gdal,sys,os
import tarfile
import gdal_merge

class LandsatLayerStack:
    def ExtractTarFile(self,infile,outdir):
        print('Start Unzip',infile)
        tar = tarfile.open(infile, "r:gz")
        tar.extractall(outdir)
        tar.close()
        return outdir
    
    def Agriculture652(self,_outnameimg,_band6,_band5,_band2):
        print('!!!!!!! Agriculture652 !!!!!!!')
        self.filename = 'B652_%s'%os.path.basename(_outnameimg)
        self.outdir = os.path.dirname(_outnameimg)
        self.band5 = _band5
        self.band6 = _band6
        self.band2 = _band2
        self.outname =  os.path.join(self.outdir,self.filename)
        self.outiff = "GTiff"
        print(self.outname)
        #sys.argv = ['-pct','-separate','-of',self.outiff,'-o',self.outname,self.band6,self.band5,self.band2]
        sys.argv = ['','-separate','-of',self.outiff,'-o',self.outname,self.band6,self.band5,self.band2]
        gdal_merge.main()
        
    def HealthyVegetation562(self,_outnameimg,_band5,_band6,_band2):
        print('!!!!!!! HealthyVegetation562 !!!!!!!')
        self.filename = 'B562_%s'%os.path.basename(_outnameimg)
        self.outdir = os.path.dirname(_outnameimg)
        self.band6 = _band6
        self.band5 = _band5
        self.band2 = _band2
        self.outname =  os.path.join(self.outdir,self.filename)
        self.outiff = "GTiff"
        print(self.outname)
        sys.argv = ['','-separate','-of',self.outiff,'-o',self.outname,self.band5,self.band6,self.band2]
        gdal_merge.main()
    def ColorInfraredVegetation543(self,_outnameimg,_band5,_band4,_band3):
        print('!!!!!!! ColorInfraredVegetation543 !!!!!!!')
        self.filename = 'B543_%s'%os.path.basename(_outnameimg)
        self.outdir = os.path.dirname(_outnameimg)
        self.band5 = _band5
        self.band4 = _band4
        self.band3 = _band3
        self.outname =  os.path.join(self.outdir,self.filename)
        self.outiff = "GTiff"
        print(self.outname)
        sys.argv = ['','-separate','-of',self.outiff,'-o',self.outname,self.band5,self.band4,self.band3]
        gdal_merge.main()
        
    def NaturalColor432(self,_outnameimg,_band4,_band3,_band2):
        print('!!!!!!! NaturalColor432 !!!!!!!')
        self.filename = 'B432_%s'%os.path.basename(_outnameimg)
        self.outdir = os.path.dirname(_outnameimg)
        self.band4 = _band4
        self.band3 = _band4
        self.band2 = _band2
        self.outname =  os.path.join(self.outdir,self.filename)
        self.outiff = "GTiff"
        print(self.outname)
        sys.argv = ['','-separate','-of',self.outiff,'-o',self.outname,self.band4,self.band3,self.band2]
        gdal_merge.main() 
              
    def BandsMergeLandsat8(self,_stadir):
        coastal_b1 = None
        blue_b2 = None
        green_b3 = None
        red_b4 = None
        nir_b5 = None
        swir1_b6 = None
        swir2_b7 = None
        panchro_b8 = None
        cirrus_b9 = None
        
        satfile = os.listdir(_stadir)
        bandlist = list()
        for img in satfile:
            chkband = str(str(img).split('_')[-1]).replace('.TIF','')
            if   chkband == 'B1':
                coastal_b1 = os.path.join(_stadir,img)
                bandlist.append(coastal_b1)
            elif chkband == 'B2':
                blue_b2= os.path.join(_stadir,img)
                bandlist.append(blue_b2)
            elif chkband == 'B3':
                green_b3= os.path.join(_stadir,img)
                bandlist.append(green_b3)
            elif chkband == 'B4':
                red_b4= os.path.join(_stadir,img)
                bandlist.append(red_b4)
            elif chkband == 'B5':
                nir_b5= os.path.join(_stadir,img)
                bandlist.append(nir_b5)
            elif chkband == 'B6':
                swir1_b6= os.path.join(_stadir,img)
                bandlist.append(swir1_b6)
            elif chkband == 'B7':
                swir2_b7= os.path.join(_stadir,img)
                bandlist.append(swir2_b7)
            elif chkband == 'B8':
                panchro_b8= os.path.join(_stadir,img)
                bandlist.append(panchro_b8)
            elif chkband == 'B9':
                cirrus_b9= os.path.join(_stadir,img)
                bandlist.append(cirrus_b9)
            else:pass    
        return bandlist

        
        
stack = LandsatLayerStack()
in1 = r'D:\Satellite\Image_Tarfile\LC81280492015333LGN00.tar.gz'
out_dir = r'D:\Satellite\Image_Raw_Extract'
fname = os.path.basename(in1)
fname = str(fname).split('.')[0]
out_dir = os.path.join(out_dir,fname)
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
print(out_dir)
instack = stack.ExtractTarFile(in1, out_dir)

satname = '%s.tiff'%fname
imgout = r'D:\Satellite\Image_Landsat8'
imgout = os.path.join(imgout,satname)
print(satname)
stacks = stack.BandsMergeLandsat8(instack)

band6 = str(stacks[5])
band5 = str(stacks[4])
band2 =str(stacks[1])
band4=str(stacks[3])
band3=str(stacks[2])


print('!!!!!!! Starting Band Merge !!!!!!!')
stack.Agriculture652(imgout, band6, band5, band2)
stack.HealthyVegetation562(imgout, band5, band6, band2)
stack.ColorInfraredVegetation543(imgout, band5, band4, band3)
stack.NaturalColor432(imgout, band4, band3, band2)
print('!!!!!!!!Done!!!!!!!!')
        