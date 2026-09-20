# 负面约束：按类别精简

负面词补充正向构造，不能代替它。按当前任务选用，避免把历史词库逐词累加。全局至少覆盖：真实/假眼、额外面具、单羽退化、生物翼；然后加当前 Form 与渲染所需项。

## 形状级眼睛意象

除禁止真实眼白、瞳孔、虹膜、眼睑和睫毛外，还必须禁止羽片边缘、接缝、阴影、高光、金属线或装饰件形成上下眼睑、眼角、杏仁形眼框、成对眼状轮廓、闭眼线或瞳孔感。不能用“没有真实眼睛”抵消表面假眼。若正向结构本身会生成上述形状，应先重写正向几何关系，再添加负面词。

## 场景几何负面

按当前场景补充：弯曲的垂直柱体、互不一致的拱券、旋纹方向错误、台面与地面不共面、人物脚底悬空、坐面穿模、栏杆与人物接触错误、前后遮挡关系错误、建筑和人物焦距透视不一致。柔焦、景深、光晕和氛围不能用来掩盖结构透视错误。

中文基础禁止项（默认按结构类别表达）：眶区出现可辨认的真实眼部结构；羽片、接缝、阴影、色块、纹样或饰件形成任何眼睛意象；贯穿覆盖层的眼形孔洞、观察缝或外露底框；单根巨羽代替多枚独立羽片；从脸部皮肤长出的生物翼。只有当前失败确实需要区分时，才展开瞳孔、虹膜、眼睑、睫毛、闭眼线、眼状斑纹等具体子类。

中文输出将下面所选形态及渲染补充项一并转为中文，避免只翻译标题。正负段使用同一语言；不同时输出中英文两套禁止项。精简时仍保留全部核心禁止范围。

英文等义基础分类（仅英文输出）：recognizable ocular anatomy within the covered orbital region; any eye imagery formed by vanes, seams, shadows, color fields, motifs or ornaments; openings, viewing slits or exposed frames through the covering; one giant feather replacing multiple distinct units; biological wings growing from facial skin。只有当前失败确实需要区分时，才展开 pupils、irises、eyelids、eyelashes、closed-eye lines 或 eyespots 等具体子类。

款式选择由服装推导，负面词只约束眼睛意象与实际结构失败。不要默认禁止宝石、方形、菱形、花丝、曲线、结饰或复杂配饰，也不要将“素面方扣、无宝石”视为通用修复。设计同质化应在方案比较阶段重设计，不能靠追加“禁止重复”代替具体正向方案。

材质负面词随当前方案选择：金属羽不禁止金属、硬质薄片或定向反光；陶瓷与玉石不禁止硬质雕片、釉面、裂纹、半透明和内反射；枝丫结构不禁止木质分叉、藤蔓或叶羽单元；琉璃羽不禁止折射；元素羽不笼统禁止特效、发光、烟雾、液体或粒子，也不强迫生成实体底板。真人皮肤的 plastic skin 等限制不得扩展到饰件。应限制厚重整块壳体取代多个羽形单元、所选遮挡机制不足而露出眼部、靠过曝或模糊掩盖眼睛、无羽形的烟团或光带，以及不符合选定材料的绒毛。隐藏底框约束不禁止贴在羽面上的可见金银装饰丝线。结构锚点缺失指没有与所选布局一致的可辨汇合、固定或幻想凝聚区域，不等于没有独立扣件；不要用负面词强迫生成珍珠或胸针。

按失败类别补充：

- 接缝：opposing feather edges enclosing almond shapes。
- 单片与受光：eye-like contours formed by a single vane, eyelid-like folds or hems, long curved shadows or highlights forming eye imagery。仅针对当前失败选用；不泛化为禁止所有渐尖羽片、织纹、折射、阴影或高光。先在正向重组实际边界、线脊与受光，不能靠追加本项代替结构修订。
- 框与填充：gold-outlined eye shapes, pale eye-shaped inlays。
- 色差：paired contrasting spindle-shaped patches over the eyes。
- 装饰：missing selected structural anchor, selected anchor hidden by feathers or hair, oversized ornament obscuring feather structure。centered 布局可写 missing central decorative connector；布局01–10改为对应侧部锚点，不得同时强制中央扣件。装饰缺失约束不能替代正向的具体材质、造型、位置和固定方式。
- 侧源布局：feathers growing biologically from the ear, temple or skin, floating lateral ornament with no attachment or coherent fantasy origin, one eye exposed, near-side eye exposed, far-side eye exposed, discontinuous coverage across the nose bridge, a single giant feather crossing both eyes, accidental symmetric eye frames, lateral flow collapsing into a headband。布局10按实际材料补充 insufficient material density over the eye region, glare or blur used to hide exposed eyes, elemental plume losing all feather-shaped or feather-flow structure, unrelated solid backing automatically inserted beneath an elemental design。

布局09金属眼羽假眼案例补充：金属描边沿眼区形成连续弧线、对称杏仁形高对比色块、中央连接把两侧边界闭合、金属线脊与蓝色填充构成装饰性眼罩。仅在布局09或相同失败证据出现时加入；不泛化为禁止金属、蓝色或中央连接。修复优先改写眼区羽面搭接和线脊走向，不能只靠加厚背衬或重复“无眼睛”禁词。

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
