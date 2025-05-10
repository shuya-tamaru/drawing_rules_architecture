import Rhino
import Rhino.DocObjects
import scriptcontext as sc
import rhinoscriptsyntax as rs
from Rhino.DocObjects import DimensionStyle, Font

def add_annotation_styles(styles):
    for name, height, scale, font_name, arrow_type, arrow_length, unit, resolution in styles:
        if rs.IsDimStyle(name):
            print(f"⚠️ 既に存在: {name}")
            continue

        dimStyleIndex = sc.doc.DimStyles.Add(name, False)
        new_dim_style = sc.doc.DimStyles[dimStyleIndex]

        new_dim_style.TextHeight = height
        new_dim_style.DimensionScale = scale
        new_dim_style.ArrowLength = arrow_length

        # 単位の設定
        new_dim_style.LengthResolution = resolution
        new_dim_style.ZeroSuppress = Rhino.DocObjects.DimensionStyle.ZeroSuppression.SuppressTrailing

        if(isinstance(unit, str) and hasattr(DimensionStyle.LengthDisplay, unit)):
            unit_enum = getattr(DimensionStyle.LengthDisplay, unit)
            new_dim_style.DimensionLengthDisplay = unit_enum
        else:
            new_dim_style.DimensionLengthDisplay = DimensionStyle.LengthDisplay.Millimeters
        

        # ArrowTypeの設定
        if isinstance(arrow_type, str) and hasattr(DimensionStyle.ArrowType, arrow_type):
            arrow_enum = getattr(DimensionStyle.ArrowType, arrow_type)
            new_dim_style.ArrowType1 = arrow_enum
            new_dim_style.ArrowType2 = arrow_enum
        elif isinstance(arrow_type, int):
            new_dim_style.ArrowType1 = DimensionStyle.ArrowType(arrow_type)
            new_dim_style.ArrowType2 = DimensionStyle.ArrowType(arrow_type)

        # Font設定
        new_dim_style.Font = Rhino.DocObjects.Font(font_name)

        # 適用
        sc.doc.DimStyles.Modify(new_dim_style, dimStyleIndex, False)
        print(f"✅ 作成: {name}（高さ: {height}, 矢印長: {arrow_length}, フォント: {font_name}）")

    sc.doc.Views.Redraw()

if __name__ == "__main__":
    # スタイルの一括登録 name, height, scale, font_name, arrow_type, arrow_length, unit, resolution
    styles = [
        ("TEXT_200", 2.5, 200, "Arial", "Dot", 2.5,"Millmeters", 1),
        ("TEXT_100", 2.5, 100, "Arial", "Dot", 2.0,"Millmeters", 1),
        ("TEXT_50", 2.5, 50, "Arial", "Dot", 1.5,"Millmeters", 1),
        ("TEXT_20", 2.5, 20, "Arial", "Dot", 1.0,"Millmeters", 1),
        ("TEXT_10", 2.5, 10, "Arial", "Dot", 0.8,"Millmeters", 1),
        ("TEXT_5", 2.5, 5, "Arial", "Dot", 0.5,"Millmeters", 1),
        ("TITLE_100", 5.0, 100, "Arial", "SolidTriangle", 2.5,"Millmeters", 1),
        ("BIGNOTE_100", 4.0, 100, "Arial", "SolidTriangle", 2.5,"Millmeters", 1),
        ("ROOMNAME_100", 3.5, 100, "MS Gothic", "Rectangle", 2.0,"Millmeters", 1),
        ("TAG_100", 3.0, 100, "MS Gothic", "Rectangle", 2.0,"Millmeters", 1),
        ("GRIDNAME_100", 3.0, 100, "MS Gothic", "Rectangle", 2.0,"Millmeters", 1),
        ("LEVELMARK_100", 2.5, 100, "MS Gothic", "Tick", 2.0,"Millmeters", 1),
        ("DETAILMARK_100", 2.5, 100, "MS Gothic", "OpenArrow", 2.0,"Millmeters", 1),
        ("NOTES_100", 2.0, 100, "MS Gothic", "ShortTriangle", 1.5,"Millmeters", 1)
    ]
    add_annotation_styles(styles)
    print("✅ 注釈スタイルの一括登録が完了しました。")
