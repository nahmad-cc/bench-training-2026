import pandas as pd

df = pd.read_csv('titanic.csv')

print("\nTITANIC ANALYSIS")
print("=" * 50)

# 1
print("\n1. Survival")
s = df['Survived'].value_counts()
print(f"Didn't survive: {s[0]} ({s[0]/len(df)*100:.1f}%)")
print(f"Survived: {s[1]} ({s[1]/len(df)*100:.1f}%)")

# 2
print("\n2. By class")
for c in [1, 2, 3]:
    fc = df[df['Pclass'] == c]
    sur = fc['Survived'].sum()
    tot = len(fc)
    print(f"Class {c}: {sur}/{tot} ({sur/tot*100:.1f}%)")

# 3
print("\n3. Average age")
died = df[df['Survived'] == 0]['Age'].mean()
lived = df[df['Survived'] == 1]['Age'].mean()
print(f"Didn't survive: {died:.1f}")
print(f"Survived: {lived:.1f}")

# 4
print("\n4. Port")
ports = df.groupby('Embarked')['Survived'].mean() * 100
for p in ports.index:
    print(f"{p}: {ports[p]:.1f}%")

# 5
print("\n5. Missing ages")
miss = df['Age'].isna().sum()
print(f"Missing: {miss} of {len(df)}")

for c in [1, 2, 3]:
    med = df[df['Pclass'] == c]['Age'].median()
    df.loc[(df['Pclass'] == c) & (df['Age'].isna()), 'Age'] = med

# 6
print("\n6. Oldest survivor")
idx = df[df['Survived'] == 1]['Age'].idxmax()
old = df.loc[idx]
print(f"{old['Name']}, {old['Age']:.0f}, Class {old['Pclass']}")

# 7
print("\n7. Gender")
w = df[df['Sex'] == 'female']['Survived'].mean() * 100
m = df[df['Sex'] == 'male']['Survived'].mean() * 100
print(f"Women: {w:.1f}%")
print(f"Men: {m:.1f}%")

# 8
print("\n8. Age groups")
def group(age):
    if age < 18:
        return 'Child'
    elif age < 60:
        return 'Adult'
    else:
        return 'Senior'

df['Group'] = df['Age'].apply(group)

for g in ['Child', 'Adult', 'Senior']:
    gdf = df[df['Group'] == g]
    r = gdf['Survived'].mean() * 100
    print(f"{g}: {r:.1f}% ({len(gdf)} people)")

# 9
print("\n9. 3rd class")
c3 = df[df['Pclass'] == 3]
w3 = c3[c3['Sex'] == 'female']['Survived'].mean() * 100
m3 = c3[c3['Sex'] == 'male']['Survived'].mean() * 100
print(f"Women: {w3:.1f}%")
print(f"Men: {m3:.1f}%")

# 10
print("\n10. Drop missing cabin")
bf = len(df)
aft = len(df.dropna(subset=['Cabin']))
print(f"{bf} -> {aft} ({aft/bf*100:.1f}%)")
