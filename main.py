import streamlit as st
import time
# import numpy as np
# import pandas as pd
# from PIL import Image

st.title('Streamlit 入門')

st.write('プログレスバーの表示')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'

toiawase1 = st.expander('問合せ1')
toiawase1.write('問合せ内容1を書く')

toiawase2 = st.expander('問合せ2')
toiawase2.write('問合せ内容2を書く')

toiawase3 = st.expander('問合せ3')
toiawase3.write('問合せ内容3を書く')

# ---------------------------------------
# ４．プログレスバー
# ---------------------------------------
# st.write('プログレスバーの表示')

# 'Start!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

# 'Done!!!!'

# ---------------------------------------
# ３．レイアウト
# ---------------------------------------

# ■ 2カラム表示
# left_column, right_column = st.columns(2)
# left_column_button = left_column.button('右カラムに文字を表示')
# if left_column_button:
#     right_column.write('ここは右カラム')

# ■ エキスパンダー
# toiawase1 = st.expander('問合せ1')
# toiawase1.write('問合せ内容1を書く')

# toiawase2 = st.expander('問合せ2')
# toiawase2.write('問合せ内容2を書く')

# toiawase3 = st.expander('問合せ3')
# toiawase3.write('問合せ内容3を書く')

# ■ サイドバー
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'コンディション：',condition
# 'あなたの趣味：',text

# ---------------------------------------
# ２．インタラクティブ
# ---------------------------------------

# ■ スライダー
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition

# ■ テキストボックス
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',text,'です'

# ■ プルダウン セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です'

# ■ チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img, caption='Noraki Nishihara', use_column_width=True)

# ---------------------------------------
# １．表示
# ---------------------------------------

# ■ イメージの表示
# img = Image.open('sample.jpg')
# st.image(img, caption='Noraki Nishihara', use_column_width=True)

# ■ サンプルデータフレームの作成（20行3列　乱数０～１　正規分布）
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# ■ MAPへのプロット
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# # ■チャートの表示
# # 折れ線グラフ
# st.line_chart(df)
# # 折れ線グラフ（塗りつぶし）
# st.area_chart(df)
# # 棒グラフ
# st.bar_chart(df)

# ■ テーブルの表示
#st.write(df, width=100, height=100)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0)) #静的

# ■ テキストの表示
# """
# # 章
# ## 節
# ### 項

# ■ プログラムソースの表示
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
