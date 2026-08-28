/**
 * Expressive Code themes reproducing Material for MkDocs code highlighting.
 *
 * The colours are the `--md-code-hl-*` variables from mkdocs-material 9.7.6
 * (`palette.min.css` for `slate`, `main.min.css` for `default`). The mapping
 * from a token to one of those colours is Material's own, read off its
 * Pygments rules in `main.min.css`:
 *
 *   k kd kn kp kr kt nd ni nl nt   keyword
 *   nc ne nf nn                    function
 *   bp nb no                       constant
 *   s* l cpf                       string
 *   cp se sh sr sx                 special
 *   m* il                          number
 *   c* sd                          comment      (docstrings included)
 *   na nv v*                       variable
 *   o ow p                         operator/punctuation
 *   n kc                           plain foreground  (True/False/None too)
 *
 * Expressive Code highlights with TextMate grammars, not Pygments, so each
 * line below is that mapping restated in the nearest TextMate scopes. Where
 * Material's value is translucent (`hsla(...)` over the code background), the
 * opaque composite is used, because a theme token colour cannot be an alpha.
 */

const dark = {
	name: 'material-slate',
	type: 'dark',
	colors: {
		'editor.background': '#272a35', // hsl(225 15% 18%)
		'editor.foreground': '#b6b9c3', // hsla(225 18% 86% / .82) composited
	},
	tokenColors: [
		{ scope: ['comment', 'punctuation.definition.comment', 'string.quoted.docstring'], settings: { foreground: '#90929a' } },
		{ scope: ['keyword', 'storage', 'storage.type', 'storage.modifier', 'keyword.control', 'entity.name.tag', 'entity.other.attribute-name', 'meta.decorator', 'punctuation.definition.decorator'], settings: { foreground: '#6791e0' } },
		{ scope: ['entity.name.function', 'entity.name.class', 'entity.name.type', 'entity.name.namespace', 'support.class', 'meta.function-call.generic'], settings: { foreground: '#c973d9' } },
		{ scope: ['support.function', 'support.type', 'support.variable', 'variable.language'], settings: { foreground: '#9383e2' } },
		{ scope: ['string', 'string.quoted', 'meta.embedded.line'], settings: { foreground: '#2fb170' } },
		{ scope: ['constant.character.escape', 'string.regexp', 'keyword.other.unit', 'meta.preprocessor'], settings: { foreground: '#f06090' } },
		{ scope: ['constant.numeric'], settings: { foreground: '#e6695b' } },
		{ scope: ['keyword.operator', 'punctuation'], settings: { foreground: '#90929a' } },
		{ scope: ['variable.other.property', 'variable.other.member', 'entity.other.attribute-name.html'], settings: { foreground: '#90929a' } },
		{ scope: ['variable', 'constant.language', 'entity.name'], settings: { foreground: '#b6b9c3' } },
	],
};

const light = {
	name: 'material-default',
	type: 'light',
	colors: {
		'editor.background': '#f5f5f5',
		'editor.foreground': '#36464e',
	},
	tokenColors: [
		{ scope: ['comment', 'punctuation.definition.comment', 'string.quoted.docstring'], settings: { foreground: '#707070' } },
		{ scope: ['keyword', 'storage', 'storage.type', 'storage.modifier', 'keyword.control', 'entity.name.tag', 'entity.other.attribute-name', 'meta.decorator', 'punctuation.definition.decorator'], settings: { foreground: '#3f6ec6' } },
		{ scope: ['entity.name.function', 'entity.name.class', 'entity.name.type', 'entity.name.namespace', 'support.class', 'meta.function-call.generic'], settings: { foreground: '#a846b9' } },
		{ scope: ['support.function', 'support.type', 'support.variable', 'variable.language'], settings: { foreground: '#6e59d9' } },
		{ scope: ['string', 'string.quoted', 'meta.embedded.line'], settings: { foreground: '#1c7d4d' } },
		{ scope: ['constant.character.escape', 'string.regexp', 'keyword.other.unit', 'meta.preprocessor'], settings: { foreground: '#db1457' } },
		{ scope: ['constant.numeric'], settings: { foreground: '#d52a2a' } },
		{ scope: ['keyword.operator', 'punctuation'], settings: { foreground: '#707070' } },
		{ scope: ['variable.other.property', 'variable.other.member', 'entity.other.attribute-name.html'], settings: { foreground: '#707070' } },
		{ scope: ['variable', 'constant.language', 'entity.name'], settings: { foreground: '#36464e' } },
	],
};

export const materialCodeThemes = [dark, light];
