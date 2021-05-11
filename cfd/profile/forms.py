from django import forms
from django.forms import widgets
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from datetimewidget.widgets import DateTimeWidget
from cfd.models import Signal, PTAAnalysis, ClassicAnalysis, Comment

class SignalForm(forms.ModelForm):
    """Form definition for Signal."""

    class Meta:
        """Meta definition for Signalform."""

        model = Signal
        fields = ('asset', 'entry_type', 'entry_point1','entry_point2', 'stop_loss1', 'stop_loss2',)
        fields += ( 'take_profit1','take_profit2', 'take_profit3', 'risk_reward', 'classic_analysis', 'pta_analysis', 'self_entered', )
        widgets = {
            #Use localization and bootstrap 3
            'signal_datetime': DateTimeWidget(usel10n=True, bootstrap_version=3),
            'entry_type': forms.widgets.RadioSelect(),
            'self_enterd': forms.widgets.RadioSelect(),
        }
        
    def __init__(self, *args, **kwargs):
        super(SignalForm, self).__init__(*args, **kwargs)
        self.fields['entry_point1'].widget.attrs.update({'placeholder': 'نقطه ورود اول (الزامی)'})
        self.fields['entry_point2'].widget.attrs.update({'placeholder': 'نقطه ورود دوم (اختیاری)'})
        self.fields['stop_loss1'].widget.attrs.update({'placeholder': 'حد اول (الزامی)'})
        self.fields['stop_loss2'].widget.attrs.update({'placeholder': 'حد دوم (اختیاری)'})
        self.fields['take_profit1'].widget.attrs.update({'placeholder': 'حد اول (الزامی)'})
        self.fields['take_profit2'].widget.attrs.update({'placeholder': 'حد دوم (اختیاری)'})
        self.fields['take_profit3'].widget.attrs.update({'placeholder': 'حد سوم (اختیاری)'})
        self.fields['classic_analysis'].queryset = ClassicAnalysis.objects.filter(signal=None)
        self.fields['pta_analysis'].queryset = PTAAnalysis.objects.filter(signal=None)
    def clean(self):
        cleaned_data = super().clean()
        # One of classic and pta analysis must be filled
        classic = cleaned_data.get('classic_analysis', None)
        pta = cleaned_data.get('pta_analysis', None)
        if not pta and not classic:
            raise ValidationError(_('برای ایجاد سیگنال باید یک تحلیل انتخاب کنید'))

class FillSignalForm(forms.ModelForm):
    class Meta:
        model = Signal
        fields = ('result_datetime', 'trade_id', 'result_pip', 'result_dollar', 'lot', 'result_image_url', 'mistakes')
        widgets = {
            'result_datetime': DateTimeWidget(usel10n=True, bootstrap_version=3)
        }
    def clean(self):
        cleaned_data = super().clean()
        # For loss signals, user must fill mistakes
        result_pip = cleaned_data.get('result_pip')
        mistakes = cleaned_data.get('mistakes')
        if result_pip and result_pip < 0:
            if not mistakes or len(mistakes) < 0:
                raise ValidationError(_('برای سیگنال‌های ضرر، اشتباهات باید حتما پر شود'))



class ChooseAnalysisForm(forms.Form):
    def __init__(self, analysis_type, *args, **kwargs):
        super(ChooseAnalysisForm, self).__init__(*args, **kwargs)
        self.analysis_type = analysis_type
        self.fields['analysis'].queryset = self.analysis_type.objects.filter(signal=None)
    analysis = forms.ModelChoiceField(queryset=None, label=_('تحلیل'))
    
class ClassicAnalysisForm(forms.ModelForm):
    class Meta:
        model = ClassicAnalysis
        fields = ('news',) # 0
        fields += ('major_trend', 'major_trend_timeframe', 'major_trend_signal',) # 1, 2, 3
        fields += ('intermediate_trend', 'intermediate_trend_timeframe', 'intermediate_trend_signal',) # 4, 5, 6
        fields += ('pattern', 'pattern_timeframe', 'pattern_signal',) # 7, 8, 9
        fields += ('moving', 'moving_timeframe', 'moving_signal',) # 10, 11, 12
        fields += ('pivot', 'pivot_timeframe', 'pivot_signal',) # 13, 14, 15
        fields += ('fibo_correction', 'fibo_signal',) # 16, 17
        fields += ('fibo_target',) # 18
        fields += ('time_divergent', 'time_divergent_timeframe', 'time_divergent_signal',) # 19, 20, 21
        fields += ('eliot', 'eliot_signal',) # 22, 23
        fields += ('candle', 'candle_timeframe', 'candle_signal',) # 24, 25, 26
        fields += ('rsi_oversold', 'rsi_overbought', 'rsi_divergence', 'rsi_hidden_divergence', 'rsi_trend_breakout', 'rsi_timeframe', 'rsi_signal',) # 27, 28, 29, 30, 31, 32, 33
        fields += ('momentum_oversold', 'momentum_overbought', 'momentum_divergence', 'momentum_hidden_divergence', 'momentum_trend_breakout', 'momentum_timeframe', 'momentum_signal',) # 34, 35, 36, 37, 38, 39, 40
        fields += ('macd_divergence', 'macd_hidden_divergence', 'macd_timeframe', 'macd_signal',) # 41, 42, 43, 44
        fields += ('stochastic_oversold', 'stochastic_overbought', 'stochastic_bullish_breakout','stochastic_bearish_breakout', 'stochastic_timeframe', 'stochastic_signal',) # 45, 46, 47, 48, 49, 50
        fields += ('atr', 'atr_timeframe', 'atr_signal',) # 51, 52, 53
        fields += ('atx', 'atx_timeframe', 'atx_signal',) # 54, 55, 56
        fields += ('image_url', 'title', 'desc', 'tradingview_url', ) # 57, 58, 59, 60
        fields += ('support_resistance1_from', 'support_resistance1_to', ) # 61, 62
        fields += ('support_resistance2_from', 'support_resistance2_to', ) # 63, 64
        fields += ('support_resistance3_from', 'support_resistance3_to', ) # 65, 66
        fields += ('support_resistance1_timeframe', 'support_resistance2_timeframe', 'support_resistance3_timeframe') # 67, 68, 69
        fields += ('support_resistance_signal', ) # 70
        widgets = {
            'major_trend': forms.widgets.RadioSelect(),
            'major_trend_signal': forms.widgets.RadioSelect(),
            'major_trend_timeframe': forms.widgets.RadioSelect(),
            'intermediate_trend': forms.widgets.RadioSelect(),
            'intermediate_trend_signal': forms.widgets.RadioSelect(),
            'intermediate_trend_timeframe': forms.widgets.RadioSelect(),
            # 'pattern': forms.widgets.RadioSelect(),
            'pattern_signal': forms.widgets.RadioSelect(),
            'pattern_timeframe': forms.widgets.RadioSelect(),
            'moving_signal': forms.widgets.RadioSelect(),
            'moving_timeframe': forms.widgets.RadioSelect(),
            'pivot': forms.widgets.RadioSelect(),
            'pivot_signal': forms.widgets.RadioSelect(),
            'pivot_timeframe': forms.widgets.RadioSelect(),
            'fibo_correction': forms.widgets.RadioSelect(),
            'fibo_signal': forms.widgets.RadioSelect(),
            'fibo_target': forms.widgets.RadioSelect(),
            'fibo_target_signal': forms.widgets.RadioSelect(),
            'time_divergent_signal': forms.widgets.RadioSelect(),
            'time_divergent_timeframe': forms.widgets.RadioSelect(),
            'eliot': forms.widgets.RadioSelect(),
            'eliot_signal': forms.widgets.RadioSelect(),
            'candle_signal': forms.widgets.RadioSelect(),
            'candle_timeframe': forms.widgets.RadioSelect(),
            'rsi_signal': forms.widgets.RadioSelect(),
            'rsi_timeframe': forms.widgets.RadioSelect(),
            'momentum_signal': forms.widgets.RadioSelect(),
            'momentum_timeframe': forms.widgets.RadioSelect(),
            'macd_signal': forms.widgets.RadioSelect(),
            'macd_timeframe': forms.widgets.RadioSelect(),
            'support_resistance_signal': forms.widgets.RadioSelect(),
            'support_resistance_timeframe': forms.widgets.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super(ClassicAnalysisForm, self).__init__(*args, **kwargs)
    
class PTAAnalysisForm(forms.ModelForm):
    class Meta:
        model = PTAAnalysis
        fields = ('any_news', 'news_detail', 'chart_move', 'impulsive_direction', 'zone_rejects', 'pattern', 'scenario', 'image_url', )


class SignalCommentForm(forms.ModelForm):
    """Form definition for SignalComment."""
    class Meta:
        """Meta definition for SignalCommentform."""
        model = Comment
        fields = ('body',)
        widgets = {'body': forms.Textarea()}
