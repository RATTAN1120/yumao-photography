# 负面约束：按类别精简

负面词补充正向构造，不能代替它。按当前任务选用，避免把历史词库逐词累加。全局至少覆盖：真实/假眼、额外面具、单羽退化、生物翼；然后加当前 Form 与渲染所需项。

中文基础禁止项（默认）：真实眼睛、眼白、瞳孔、虹膜、眼睑或睫毛可见；羽毛拼出的眼睛；整个眼羽及配饰上的任何眼睛意象，包括闭眼线、眼形孔洞或轮廓、眼睑状接缝、眼形阴影或色块、眼状斑纹、抽象眼睛符号、眼形饰件；羽毛下露出的眼孔面具或底框；单根巨羽代替多枚独立羽片；从脸部皮肤长出的生物翼。

中文输出将下面所选形态及渲染补充项一并转为中文，避免只翻译标题。正负段使用同一语言；不同时输出中英文两套禁止项。精简时仍保留全部核心禁止范围。

英文等义基础词组（仅英文输出）：visible eyes, exposed sclera or irises or pupils, visible eyelids or eyelashes, eyes assembled from feathers, eye imagery anywhere on the feather covering or its ornaments, closed-eye lines, eye-shaped openings or outlines or markings, eyelid-shaped seams, eye-like shadows or color patches, eyespots, abstract eye symbols, eye-shaped jewelry, visible eye-mask frames beneath feathers, single giant feather replacing multiple feathers, biological wings growing from the face。精简输出也必须保留真实眼部细节、羽毛拼眼及任何眼睛意象的禁止范围。

款式选择由服装推导，负面词只约束眼睛意象与实际结构失败。不要默认禁止宝石、方形、菱形、花丝、曲线、结饰或复杂配饰，也不要将“素面方扣、无宝石”视为通用修复。设计同质化应在方案比较阶段重设计，不能靠追加“禁止重复”代替具体正向方案。

材质负面词随当前方案选择：金属羽不禁止金属、硬质薄片或定向反光；琉璃羽不禁止折射；元素羽不笼统禁止特效、发光或粒子。真人皮肤的 plastic skin 等限制不得扩展到饰件。可分别限制厚重整块壳体取代独立羽片、透明材料透出眼部、过曝掩盖结构、无羽形的烟团以及不符合选定材料的绒毛。隐藏底框约束不禁止贴在羽面上的可见金银装饰丝线。结构锚点缺失指没有与所选布局一致的可辨汇合或固定区域，不等于没有独立扣件；不要用负面词强迫生成珍珠或胸针。

按失败类别补充：

- 接缝：opposing feather edges enclosing almond shapes。
- 框与填充：gold-outlined eye shapes, pale eye-shaped inlays。
- 色差：paired contrasting spindle-shaped patches over the eyes。
- 装饰：missing selected structural anchor, selected anchor hidden by feathers or hair, oversized ornament obscuring feather structure。centered 布局可写 missing central decorative connector；布局01–10改为对应侧部锚点，不得同时强制中央扣件。装饰缺失约束不能替代正向的具体材质、造型、位置和固定方式。
- 侧源布局：feathers growing biologically from the ear, temple or skin, floating lateral ornament with no attachment, one eye exposed, near-side eye exposed, far-side eye exposed, discontinuous coverage across the nose bridge, a single giant feather crossing both eyes, accidental symmetric eye frames, lateral flow collapsing into a headband。布局10另加 effects replacing the opaque eye-covering layer, glare used to hide exposed eyes, elemental plume losing all feather-shaped structure。

不是一律禁止中央珠宝、金银线、辅色、对称、羽轴和阴影；它们不得在整个眼羽及配饰上构成任何眼睛意象，即使单侧、非闭合或不在真实眼位也不例外。不要使用泛化的 butterfly-shaped 或 wing-shaped 禁掉已认可的整体外轮廓；另按当前 Form 限制实际形态偏离。

| Form | 针对性失败项 | 不可误禁 |
| --- | --- | --- |
| closed | excessive vertical fan, missing tapered lateral extensions | 适中侧向外延 |
| open | bulky feather mass replacing angular spread, disconnected central covering | 外羽张角和展开 |
| draped | detached hanging feather strands, horizontal viewing slit, short fringe replacing drapes | 连续下弯、自然羽间层次 |
| wrap | flat goggle shell, isolated temple patch, exposed near-side eye | 后掠、弧向长度、远侧遮挡 |

真人/COS按需加入：childlike proportions, extra limbs, extra fingers, fused hands, distorted joints, stretched torso, unnaturally elongated legs, plastic skin, cheap wig, fabric intersections, over-sharpening。二次元用成熟比例、解剖与服装结构词，不禁止 anime；3D不禁止 CGI、PBR。材质限定对象，如 plastic skin 不否定用户指定塑料饰品。图案服装不禁 printed costume。

人体负面词按当前画面选用：额外或重复手臂、腿、手掌或脚；无法连接肩髋的孤立手足；同一袖口长出多只手；分叉肢体；融合或额外手指、脚趾；断裂或反折关节；手与道具穿模。负面词不能代替主文件的肢体连接检查；正常遮挡和画外肢体不等于缺肢，抓握时不可见的手指不等于少指，不要求全身或全部指趾强行入镜。

完整构图时加入 cropped crown, clipped feather tips, cut-off feet（仅全身要求）。用户指定局部裁切则不添加冲突项。无文字需求时可排除 watermark、unwanted text；场景合理标识与用户指定文字按任务处理。

输出前比对实际正向，删除否定目标方向、材质、饰件和裁切的词。不能只因词库有某词就机械输出。
