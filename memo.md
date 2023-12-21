# 📝 2023/12/21

## macOS のapp に近づける

1. `categories.plist` で一覧出す
1. `symbol_search.plist` でフィルター

この流れかな？


# 📝 2023/12/15

## iOS 17.2
```
symbol_categories.plist: 5648
symbol_search.plist: 2247
legacy_flippable.plist: 75
name_availability.plist: 2
Info.plist: 22
categories.plist: 31
symbol_order.plist: 6153

```



# 📝 2023/08/07

[https://github.com/mikaelho/pythonista-misc/blob/master/sfsymbol%202.py](https://github.com/mikaelho/pythonista-misc/blob/master/sfsymbol%202.py)

# 📝 2023/08/06


## iOS
```
symbol_categories.plist: 4375
symbol_search.plist: 1925
legacy_flippable.plist: 75
name_availability.plist: 2
Info.plist: 22
categories.plist: 30
symbol_order.plist: 4824

```

## macOS

```
Info.plist: 20
version.plist: 5
symbol_categories.plist: 2888
symbol_search.plist: 1584
legacy_flippable.plist: 75
name_availability.plist: 2
categories.plist: 23
symbol_order.plist: 3524
```

## 比較


| No. | name | iOS | macOS |
| ---- | ---- | ---- | ---- |
| 1 | Info.plist | 22 | 20 |
| 2 | symbol_order.plist | 4824 | 3524 |
| 3 | symbol_categories.plist | 4375 | 2888 |
| 4 | symbol_search.plist | 1925 | 1584 |
| 5 | legacy_flippable.plist | 75 | 75 |
| 6 | categories.plist | 30 | 23 |
| 7 | name_availability.plist | 2 | 2 |

(`.json` リンクつける)

# 📝 2023/08/05

[Get list of SF Symbol names in code | Apple Developer Forums](https://developer.apple.com/forums/thread/695321)

```
/System/Library/CoreServices/CoreGlyphs.bundle
```






# 📝 2023/08/04


[SFSymbols? | omz:forum](https://forum.omz-software.com/topic/6002/sfsymbols/37)

```
CoreGlyphs.bundle
 ├── symbol_categories.plist
 ├── symbol_search.plist
 ├── _CodeSignature
 │	├── CodeRequirements-1
 │	├── CodeSignature
 │	├── CodeResources
 │	├── CodeDirectory
 │	└── CodeRequirements
 ├── legacy_flippable.plist
 ├── nofill_to_fill.strings
 ├── name_availability.plist
 ├── Info.plist
 ├── symbol_restrictions.strings
 ├── name_aliases.strings
 ├── semantic_to_descriptive_name.strings
 ├── Assets.car
 ├── categories.plist
 └── symbol_order.plist


```
