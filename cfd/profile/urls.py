from django.urls import path
from cfd.profile import views

urlpatterns = [
    path('team/<team_id>/signals/all/', views.signals_all, name='cfd_profile_signals_all_view'),
    path('team/<team_id>/signals/', views.signals_month, name='cfd_profile_signals_month_view'),
    path('team/<team_id>/signals/add/', views.add_signal, name='cfd_profile_signals_add'),
    path('signals/<signal_id>/analysis/classic/choose/', views.choose_classic_analysis, name='cfd_profile_analysis_classic_choose'),
    path('signals/<signal_id>/analysis/pta/choose/', views.choose_pta_analysis, name='cfd_profile_analysis_pta_choose'),
    path('signals/<signal_id>/analysis/classic/remove/', views.remove_classic_analysis, name='cfd_profile_analysis_classic_remove'),
    path('signals/<signal_id>/analysis/pta/remove/', views.remove_pta_analysis, name='cfd_profile_analysis_pta_remove'),
    path('signals/<signal_id>/', views.signal_info, name='cfd_profile_signals_info'),
    path('signals/<signal_id>/fill/', views.fill_signal, name='cfd_profile_signals_fill'),
    # path('signals/<signal_id>/cancel/', views.cancel_signal, name='cfd_profile_signals_cancel'),
    path('signals/<signal_id>/events/add/', views.add_signal_event, name='cfd_profile_signal_events_add'),
    path('signals/<signal_id>/result/', views.signal_result, name='cfd_profile_signals_result'),
    path('signals/<signal_id>/mistakes/append/', views.append_signal_mistakes, name='cfd_profile_mistakes_append'),
    path('team/<team_id>/signals/mistakes/', views.view_mistakes, name='cfd_profile_signals_mistakes'),
    path('team/<team_id>/analysis/classic/', views.view_classic_analysis, name='cfd_profile_analysis_classic_view'),
    path('team/<team_id>/analysis/pta/', views.view_pta_analysis, name='cfd_profile_analysis_pta_view'),
    path('team/<team_id>/analysis/classic/add/', views.add_classic_analysis, name='cfd_profile_analysis_classic_add'),
    path('team/<team_id>/analysis/pta/add/', views.add_pta_analysis, name='cfd_profile_analysis_pta_add'),
    path('analysis/classic/<int:analysis_id>/', views.classic_analysis_info, name='cfd_profile_analysis_classic_info'),
    path('analysis/pta/<int:analysis_id>/', views.pta_analysis_info, name='cfd_profile_analysis_pta_info'),
    path('analysis/classic/<int:analysis_id>/edit', views.classic_analysis_edit, name='cfd_profile_analysis_classic_edit'),
    path('analysis/pta/<int:analysis_id>/edit', views.pta_analysis_edit, name='cfd_profile_analysis_pta_edit'),
    path('analysis/classic/<int:analysis_id>/delete', views.classic_analysis_delete, name='cfd_profile_analysis_classic_delete'),
    path('analysis/pta/<int:analysis_id>/delete', views.pta_analysis_delete, name='cfd_profile_analysis_pta_delete'),
    path('signals/<int:signal_id>/evaluations/', views.signal_evaluation_list, name='cfd_profile_signal_evaluations_list'),
    path('signals/<int:signal_id>/evaluations/add/', views.signal_evaluation_add, name='cfd_profile_signal_evaluations_add'),
    path('signals/evaluations/<int:signaleval_id>/edit/', views.signal_evaluation_edit, name='cfd_profile_signal_evaluations_edit'),
    path('signals/evaluations/<int:signaleval_id>/delete/', views.signal_evaluation_delete, name='cfd_profile_signal_evaluations_delete'),
    path('evaluations/<int:team_id>/', views.evaluation_list, name='cfd_profile_evaluations_list'),
    path('evaluations/<int:team_id>/add/', views.evaluation_add, name='cfd_profile_evaluations_add'),
    path('evaluations/<int:evaluation_id>/edit/', views.evaluation_edit, name='cfd_profile_evaluations_edit'),
    path('evaluations/<int:evaluation_id>/delete/', views.evaluation_delete, name='cfd_profile_evaluations_delete'),
    # path('report/rep1/', views.user_summary, name='cfd_profile_report_rep1'),
    # path('report/test/', views.test, name='cfd_profile_report_rep1'),
]