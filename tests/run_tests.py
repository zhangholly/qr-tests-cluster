import os, sys
from libtbx import easy_run
from iotbx import pdb

import run_finalise

pdbs = {"PRO_terminal" : """
CRYST1   42.664   49.718   66.065 109.25  94.96  99.24 P 1           4
ATOM    874  N   PRO A 115      -9.167  -7.159   4.783  1.00 30.39           N
ATOM    875  CA  PRO A 115      -9.350  -8.630   5.081  1.00 30.17           C
ATOM    876  C   PRO A 115      -9.382  -9.587   3.862  1.00 32.77           C
ATOM    877  O   PRO A 115     -10.069  -9.304   2.880  1.00 33.78           O
ATOM    878  CB  PRO A 115     -10.669  -8.662   5.838  1.00 28.12           C
ATOM    879  CG  PRO A 115     -10.665  -7.351   6.592  1.00 29.06           C
ATOM    880  CD  PRO A 115     -10.013  -6.329   5.660  1.00 30.28           C
ATOM    881  N  AGLY A 116      -8.745 -10.760   4.020  0.50 31.15           N
ATOM    882  CA AGLY A 116      -8.770 -11.833   3.012  0.50 27.99           C
ATOM    883  C  AGLY A 116      -7.959 -13.081   3.370  0.50 26.73           C
ATOM    884  O  AGLY A 116      -7.545 -13.840   2.487  0.50 26.23           O
ATOM    885  N  BGLY A 116      -8.621 -10.686   3.937  0.50 35.25           N
ATOM    886  CA BGLY A 116      -8.079 -11.393   2.744  0.50 36.56           C
ATOM    887  C  BGLY A 116      -8.989 -12.091   1.734  0.50 36.99           C
ATOM    888  O  BGLY A 116      -9.994 -11.547   1.293  0.50 37.57           O
ATOM    889  N  AGLY A 117      -7.748 -13.313   4.661  0.50 25.75           N
ATOM    890  CA AGLY A 117      -6.947 -14.457   5.099  0.50 24.75           C
ATOM    891  C  AGLY A 117      -5.660 -14.520   4.307  0.50 24.36           C
ATOM    892  O  AGLY A 117      -5.284 -13.541   3.660  0.50 23.17           O
ATOM    893  N  BGLY A 117      -8.582 -13.285   1.315  0.50 36.89           N
ATOM    894  CA BGLY A 117      -9.277 -14.011   0.264  0.50 35.40           C
ATOM    895  C  BGLY A 117      -8.318 -14.993  -0.358  0.50 37.53           C
ATOM    896  O  BGLY A 117      -8.109 -14.988  -1.568  0.50 39.46           O
ATOM    897  N  ASER A 118      -4.970 -15.660   4.366  0.50 25.06           N
ATOM    898  CA ASER A 118      -3.753 -15.855   3.578  0.50 25.99           C
ATOM    899  C  ASER A 118      -3.903 -15.046   2.311  0.50 28.77           C
ATOM    900  O  ASER A 118      -4.893 -15.203   1.584  0.50 30.82           O
ATOM    901  CB ASER A 118      -3.569 -17.326   3.226  0.50 24.41           C
ATOM    902  OG ASER A 118      -4.540 -17.742   2.278  0.50 25.05           O
ATOM    903  N  BSER A 118      -7.724 -15.839   0.481  0.50 38.64           N
ATOM    904  CA BSER A 118      -6.635 -16.713   0.055  0.50 38.40           C
ATOM    905  C  BSER A 118      -5.353 -15.909  -0.093  0.50 39.49           C
ATOM    906  O  BSER A 118      -4.263 -16.472  -0.176  0.50 39.26           O
ATOM    907  CB BSER A 118      -6.980 -17.441  -1.256  0.50 37.71           C
ATOM    908  OG BSER A 118      -8.020 -16.788  -1.972  0.50 34.61           O
""",
  'helix' : """
CRYST1   16.291   18.744   30.715  90.00  90.00  90.00 P 1
SCALE1      0.061384  0.000000  0.000000        0.00000
SCALE2      0.000000  0.053350  0.000000        0.00000
SCALE3      0.000000  0.000000  0.032557        0.00000
ATOM      1  N   GLY A  87       6.046  11.922   5.000  1.00 80.00           N
ATOM      2  CA  GLY A  87       6.777  11.037   5.889  1.00 80.00           C
ATOM      3  C   GLY A  87       7.208  11.727   7.197  1.00 80.00           C
ATOM      4  O   GLY A  87       7.552  11.016   8.143  1.00 80.00           O
ATOM      5  HA2 GLY A  87       6.151  10.181   6.142  1.00 80.00           H
ATOM      6  HA3 GLY A  87       7.670  10.673   5.382  1.00 80.00           H
ATOM      7  HT1 GLY A  87       5.481  11.402   4.424  1.00 80.00           H
ATOM      8  HT2 GLY A  87       6.362  12.695   4.526  1.00 80.00           H
ATOM      9  N   GLY A  88       7.248  13.042   7.248  1.00 80.00           N
ATOM     10  CA  GLY A  88       7.861  13.744   8.387  1.00 80.00           C
ATOM     11  C   GLY A  88       7.082  13.437   9.673  1.00 80.00           C
ATOM     12  O   GLY A  88       7.692  13.174  10.712  1.00 80.00           O
ATOM     13  H   GLY A  88       6.872  13.660   6.529  1.00 80.00           H
ATOM     14  HA2 GLY A  88       8.894  13.419   8.512  1.00 80.00           H
ATOM     15  HA3 GLY A  88       7.847  14.820   8.212  1.00 80.00           H
ATOM     16  N   GLY A  89       5.753  13.529   9.640  1.00 80.00           N
ATOM     17  CA  GLY A  89       5.000  13.335  10.878  1.00 80.00           C
ATOM     18  C   GLY A  89       5.204  11.952  11.421  1.00 80.00           C
ATOM     19  O   GLY A  89       5.421  11.767  12.629  1.00 80.00           O
ATOM     20  H   GLY A  89       5.191  13.727   8.812  1.00 80.00           H
ATOM     21  HA2 GLY A  89       5.328  14.057  11.626  1.00 80.00           H
ATOM     22  HA3 GLY A  89       3.937  13.484  10.690  1.00 80.00           H
ATOM     23  N   GLY A  90       5.138  10.940  10.551  1.00 80.00           N
ATOM     24  CA  GLY A  90       5.317   9.584  11.016  1.00 80.00           C
ATOM     25  C   GLY A  90       6.702   9.325  11.564  1.00 80.00           C
ATOM     26  O   GLY A  90       6.869   8.577  12.510  1.00 80.00           O
ATOM     27  H   GLY A  90       4.967  11.033   9.550  1.00 80.00           H
ATOM     28  HA2 GLY A  90       4.592   9.374  11.802  1.00 80.00           H
ATOM     29  HA3 GLY A  90       5.140   8.893  10.192  1.00 80.00           H
ATOM     30  N   GLY A  91       7.717   9.953  10.967  1.00 80.00           N
ATOM     31  CA  GLY A  91       9.078   9.825  11.482  1.00 80.00           C
ATOM     32  C   GLY A  91       9.167  10.416  12.883  1.00 80.00           C
ATOM     33  O   GLY A  91       9.768   9.836  13.795  1.00 80.00           O
ATOM     34  H   GLY A  91       7.631  10.546  10.141  1.00 80.00           H
ATOM     35  HA2 GLY A  91       9.362   8.774  11.523  1.00 80.00           H
ATOM     36  HA3 GLY A  91       9.773  10.354  10.830  1.00 80.00           H
ATOM     37  N   GLY A  92       8.569  11.589  13.066  1.00 80.00           N
ATOM     38  CA  GLY A  92       8.571  12.212  14.379  1.00 80.00           C
ATOM     39  C   GLY A  92       7.807  11.339  15.374  1.00 80.00           C
ATOM     40  O   GLY A  92       8.274  11.127  16.495  1.00 80.00           O
ATOM     41  H   GLY A  92       8.086  12.120  12.341  1.00 80.00           H
ATOM     42  HA2 GLY A  92       9.595  12.336  14.730  1.00 80.00           H
ATOM     43  HA3 GLY A  92       8.094  13.191  14.327  1.00 80.00           H
ATOM     44  N   GLY A  93       6.648  10.831  14.954  1.00 80.00           N
ATOM     45  CA  GLY A  93       5.852  10.007  15.846  1.00 80.00           C
ATOM     46  C   GLY A  93       6.543   8.707  16.220  1.00 80.00           C
ATOM     47  O   GLY A  93       6.368   8.241  17.352  1.00 80.00           O
ATOM     48  H   GLY A  93       6.247  10.970  14.026  1.00 80.00           H
ATOM     49  HA2 GLY A  93       5.644  10.561  16.761  1.00 80.00           H
ATOM     50  HA3 GLY A  93       4.903   9.766  15.366  1.00 80.00           H
ATOM     51  N   GLY A  94       7.316   8.108  15.306  1.00 80.00           N
ATOM     52  CA  GLY A  94       8.069   6.911  15.672  1.00 80.00           C
ATOM     53  C   GLY A  94       9.095   7.229  16.749  1.00 80.00           C
ATOM     54  O   GLY A  94       9.242   6.502  17.717  1.00 80.00           O
ATOM     55  H   GLY A  94       7.436   8.416  14.341  1.00 80.00           H
ATOM     56  HA2 GLY A  94       7.389   6.147  16.049  1.00 80.00           H
ATOM     57  HA3 GLY A  94       8.588   6.519  14.797  1.00 80.00           H
ATOM     58  N   GLY A  95       9.799   8.362  16.572  1.00 80.00           N
ATOM     59  CA  GLY A  95      10.718   8.799  17.602  1.00 80.00           C
ATOM     60  C   GLY A  95       9.986   9.053  18.925  1.00 80.00           C
ATOM     61  O   GLY A  95      10.478   8.633  19.982  1.00 80.00           O
ATOM     62  H   GLY A  95       9.748   8.967  15.753  1.00 80.00           H
ATOM     63  HA2 GLY A  95      11.479   8.036  17.764  1.00 80.00           H
ATOM     64  HA3 GLY A  95      11.208   9.721  17.290  1.00 80.00           H
ATOM     65  N   GLY A  96       8.848   9.743  18.892  1.00 80.00           N
ATOM     66  CA  GLY A  96       8.100   9.974  20.115  1.00 80.00           C
ATOM     67  C   GLY A  96       7.693   8.670  20.785  1.00 80.00           C
ATOM     68  O   GLY A  96       7.804   8.505  21.994  1.00 80.00           O
ATOM     69  H   GLY A  96       8.430  10.144  18.053  1.00 80.00           H
ATOM     70  HA2 GLY A  96       8.710  10.548  20.813  1.00 80.00           H
ATOM     71  HA3 GLY A  96       7.199  10.545  19.890  1.00 80.00           H
ATOM     72  N   GLY A  97       7.185   7.734  19.986  1.00 80.00           N
ATOM     73  CA  GLY A  97       6.758   6.466  20.521  1.00 80.00           C
ATOM     74  C   GLY A  97       7.928   5.704  21.152  1.00 80.00           C
ATOM     75  O   GLY A  97       7.822   5.143  22.238  1.00 80.00           O
ATOM     76  H   GLY A  97       7.062   7.832  18.978  1.00 80.00           H
ATOM     77  HA2 GLY A  97       5.995   6.627  21.282  1.00 80.00           H
ATOM     78  HA3 GLY A  97       6.333   5.856  19.724  1.00 80.00           H
ATOM     79  N   GLY A  98       9.077   5.703  20.473  1.00 80.00           N
ATOM     80  CA  GLY A  98      10.259   5.038  20.999  1.00 80.00           C
ATOM     81  C   GLY A  98      10.776   5.677  22.259  1.00 80.00           C
ATOM     82  O   GLY A  98      11.190   5.000  23.207  1.00 80.00           O
ATOM     83  H   GLY A  98       9.215   6.150  19.567  1.00 80.00           H
ATOM     84  HA2 GLY A  98      10.022   3.996  21.214  1.00 80.00           H
ATOM     85  HA3 GLY A  98      11.051   5.063  20.251  1.00 80.00           H
ATOM     86  N   GLY A  99      10.812   6.998  22.323  1.00 80.00           N
ATOM     87  CA  GLY A  99      11.291   7.723  23.477  1.00 80.00           C
ATOM     88  C   GLY A  99      10.302   7.784  24.656  1.00 80.00           C
ATOM     89  O   GLY A  99      10.656   8.287  25.715  1.00 80.00           O
ATOM     90  OXT GLY A  99       9.077   7.282  24.507  1.00 80.00           O
ATOM     91  H   GLY A  99      10.505   7.607  21.565  1.00 80.00           H
ATOM     92  HA2 GLY A  99      12.210   7.256  23.832  1.00 80.00           H
ATOM     93  HA3 GLY A  99      11.525   8.746  23.181  1.00 80.00           H
ATOM     94  HXT GLY A  99       8.983   6.901  23.568  1.00 80.00           H
TER
END
""",
        }

def test_PRO_terminal_and_alt_loc():
  tf = 'PRO_terminal.pdb'
  f=file(tf, "wb")
  f.write(pdbs["PRO_terminal"])
  f.close()
  cmd = 'iotbx.python ../run_finalise.py %s' % tf
  print cmd
  easy_run.call(cmd)
  pdb_inp = pdb.input(tf.replace('.pdb', '_complete.pdb'))
  hierarchy = pdb_inp.construct_hierarchy()
  must_find = ['H2', 'H3', 'OXT']
  for atom in hierarchy.atoms():
    assert atom.name.strip()!='H1'
    if atom.name.strip() in must_find:
      must_find.remove(atom.name.strip())
  assert not must_find
  print 'OK'

def test_1yjp_charge():
  pdb_inp = pdb.input('1yjp.pdb')
  hierarchy = pdb_inp.construct_hierarchy()
  try:
    charge = run_finalise.calculate_pdb_hierarchy_charge(hierarchy)
    assert 0
  except Exception, e:
    assert e.message.find('no hydrogens')>-1
  print 'OK'
  tf='1yjp.pdb'
  cmd = 'iotbx.python ../run_finalise.py %s' % tf
  print cmd
  easy_run.call(cmd)
  pdb_inp = pdb.input(tf.replace('.pdb', '_complete.pdb'))
  hierarchy = pdb_inp.construct_hierarchy()
  charge = run_finalise.calculate_pdb_hierarchy_charge(hierarchy, verbose=1)
  print 'charge',charge
  assert charge==0, 'charge of 1yjp should be zero not %s' % charge
  print 'OK'

def test_helix():
  tf = 'helix.pdb'
  f=file(tf, "wb")
  f.write(pdbs["helix"])
  f.close()
  pdb_inp=pdb.input(tf)
  hierarchy = pdb_inp.construct_hierarchy()
  charge = run_finalise.calculate_pdb_hierarchy_charge(hierarchy, verbose=1)
  print 'charge',charge
  assert charge==0, 'charge of helix should be zero not %s' % charge
  print 'OK'
  cmd = 'iotbx.python ../run_finalise.py %s' % tf
  print cmd
  easy_run.call(cmd)
  pdb_inp = pdb.input(tf.replace('.pdb', '_complete.pdb'))
  hierarchy = pdb_inp.construct_hierarchy()
  must_find = ['H1', 'H2', 'H3', 'OXT']
  for atom in hierarchy.atoms():
    if atom.name.strip() in must_find:
      must_find.remove(atom.name.strip())
  assert not must_find
  print 'OK'
  pdb_inp=pdb.input(tf.replace('.pdb', '_complete.pdb'))
  hierarchy = pdb_inp.construct_hierarchy()
  charge = run_finalise.calculate_pdb_hierarchy_charge(hierarchy, verbose=1)
  print 'charge',charge
  assert charge==1, 'charge of helix should be one not %s' % charge
  print 'OK'

def run():
  test_PRO_terminal_and_alt_loc()
  test_1yjp_charge()
  test_helix()

if __name__=="__main__":
  args = sys.argv[1:]
  del sys.argv[1:]
  run(*tuple(args))