# CircleMenu
�Զ���ViewGroupʵ�ֵ�Բ����ת�˵���֧�ָ�����ָ��ת�Լ�������ת��
ͼ���������á�

�÷�
=====
1�������ļ��������ؼ�

	<com.zhy.view.CircleMenuLayout
		android:id="@+id/id_menulayout"
		android:layout_width="match_parent"
		android:layout_height="match_parent"
		android:padding="100dp"
		android:background="@drawable/circle_bg3" >
	</com.zhy.view.CircleMenuLayout>

2��Activity��onCreate��|Fragment��onCreateView��

	public class CircleActivity extends Activity
	{
		private CircleMenuLayout mCircleMenuLayout;

		private String[] mItemTexts = new String[] { "��ȫ���� ", "��ɫ����", "Ͷ�����",
				"ת�˻��", "�ҵ��˻�", "���ÿ�" };
		private int[] mItemImgs = new int[] { R.drawable.home_mbank_1_normal,
				R.drawable.home_mbank_2_normal, R.drawable.home_mbank_3_normal,
				R.drawable.home_mbank_4_normal, R.drawable.home_mbank_5_normal,
				R.drawable.home_mbank_6_normal };

		@Override
		protected void onCreate(Bundle savedInstanceState)
		{
			super.onCreate(savedInstanceState);
			
			//�����л������ļ���Ч��
			setContentView(R.layout.activity_main02);

			mCircleMenuLayout = (CircleMenuLayout) findViewById(R.id.id_menulayout);
			mCircleMenuLayout.setMenuItemIconsAndTexts(mItemImgs, mItemTexts);
		}

	}

3����ӵ���¼�

	mCircleMenuLayout.setOnMenuItemClickListener(new OnMenuItemClickListener()
	{
		@Override
		public void itemClick(View view, int pos)
		{
			Toast.makeText(CircleActivity.this, mItemTexts[pos],
					Toast.LENGTH_SHORT).show();

		}
		@Override
		public void itemCenterClick(View view)
		{
			Toast.makeText(CircleActivity.this,
					"you can do something just like ccb  ",
					Toast.LENGTH_SHORT).show();
		}
	});

Ч��ͼ
=====

CircleMenuSample

![Sample Screenshots][1]

CCBSample ע��ǧ�������Ϊʲô��һ�飬���о��������ġ�

![Sample Screenshots][2]


������
=====

[�ҵĲ��͵�ַ][3]


[1]: https://github.com/hongyangAndroid/CircleMenu/blob/master/sample_zhy_CircleMenu/screen_shot.gif
[2]: https://github.com/hongyangAndroid/CircleMenu/blob/master/sample_zhy_CircleMenu/ccb.gif
[3]: http://blog.csdn.net/lmj623565791
