from django.db import models
import math
import decimal

# Create your models here.
class CatWise(models.Model):
    RaDEC = models.CharField(max_length=50)
    RA = models.DecimalField(max_digits=15,decimal_places=9)
    DEC = models.DecimalField(max_digits=15,decimal_places=9)
    FoundInSearch = models.CharField(max_length=100)
    AddDate = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    w1mpro = models.DecimalField(max_digits=11,decimal_places=6)
    w1sigmpro = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    w1snr_pm = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    w2mpro = models.DecimalField(max_digits=11,decimal_places=6)
    w2sigmpro = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    w2snr_pm = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)

    PMRA = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    sigPMRA = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    PMDec = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    sigPMDec = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    GaiaDR2plx = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True) 
    GaiaDR2PlxErr = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    SIMBAD = models.BooleanField()

    BYW = models.CharField(max_length=50,blank=True,null=True)
    GaiaCoMover = models.BooleanField(blank=True,null=True)
    OnSpitzerPrg = models.CharField(max_length=50, blank=True,null=True)

    JMag = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    JMagErr = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    JMagSrc = models.CharField(max_length=50,blank=True,null=True)
    CatWISESpec = models.CharField(max_length=50,blank=True,null=True)
    CatWISESpecSrc = models.CharField(max_length=50,blank=True,null=True)
    SpizerConsider = models.BooleanField(blank=True,null=True)

    VTan = models.DecimalField(max_digits=18,decimal_places=10,blank=True,null=True)
    JW2Diff = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    JW2DiffErr = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    W1W2Diff = models.DecimalField(max_digits=11,decimal_places=6,blank=True)
    W1W2DiffErr = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    TotalPM = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    TotalPMErr = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    H_W2 = models.DecimalField(max_digits=11,decimal_places=6,blank=True,null=True)
    WiseURL = models.URLField(blank=True)
    
    Note = models.TextField(blank=True,null=True)

    # How the object should be displayed in the admin console.
    def __str__(self):
        return self.FoundInSearch + " ~ [RADEC: " + self.RaDEC + " ]"

    # How to calculate other fields given values
    def save(self,*args,**kwargs):
        if self.PMRA and self.PMDec and self.GaiaDR2plx:
            self.VTan = decimal.Decimal(4.74) * decimal.Decimal(math.sqrt((self.PMRA**2) + (self.PMDec**2))) / (self.GaiaDR2plx/1000)
        if self.JMag:
            self.JW2Diff = self.JMag - self.w2mpro
        if self.JMagErr:
            self.JW2DiffErr = decimal.Decimal(math.sqrt((self.w2sigmpro**2) + (self.JMagErr**2)))
        self.W1W2Diff = self.w1mpro - self.w2mpro
        if self.w1sigmpro and self.w2sigmpro:
            self.W1W2DiffErr = decimal.Decimal(math.sqrt((self.w1sigmpro**2) + (self.w2sigmpro**2)))
        if self.PMRA and self.PMDec:
            self.TotalPM = decimal.Decimal(math.sqrt((self.PMRA**2) + (self.PMDec**2)))
        if self.sigPMRA and self.sigPMDec:
            self.TotalPMErr = decimal.Decimal(math.sqrt((self.sigPMRA**2) + (self.sigPMDec**2)))
        if self.TotalPM:
            self.H_W2 = self.w2mpro + 5 + 5*decimal.Decimal(math.log10(self.TotalPM))
        self.WiseURL = f"http://byw.tools/wiseview#ra={self.RA}&dec={self.DEC}&size=120.000&band=3&speed=200&trimbright=75&linear=1&color=gray&mode=fixed&coadd_mode=window-1.0-year&zoom=9"
        super(CatWise,self).save(*args,**kwargs)
