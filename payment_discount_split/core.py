import math,itertools
from decimal import Decimal
from fractions import Fraction
from .common import integer,identifier,unique_ids
def run(d):
 rows=d['lines'];unique_ids(rows);basis=integer(d['discount_basis_points'],0,10000)
 if not 1<=len(rows)<=10000:raise ValueError('lines')
 amounts=[integer(r['cents'],0,10**12)for r in rows];total=sum(amounts);exact=Fraction(total*basis,10000);rounded=(2*exact.numerator+exact.denominator)//(2*exact.denominator);quotas=[Fraction(v*basis,10000)for v in amounts];alloc=[q.numerator//q.denominator for q in quotas];remaining=rounded-sum(alloc)
 order=sorted(range(len(rows)),key=lambda i:(-(quotas[i]-alloc[i]),rows[i]['id']))
 for i in order[:remaining]:alloc[i]+=1
 return dict(gross_cents=total,discount_cents=rounded,payable_cents=total-rounded,lines=[dict(id=r['id'],gross_cents=v,discount_cents=a,payable_cents=v-a)for r,v,a in zip(rows,amounts,alloc)],rounding='half_up_total_largest_remainder_tie_by_id')
