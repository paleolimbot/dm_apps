from django.views.generic import TemplateView, DetailView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from whalesdb import forms, models, filters, utils
from django.contrib.auth.mixins import UserPassesTestMixin
from shared_models.views import CommonTemplateView, CommonAuthCreateView, CommonAuthUpdateView, CommonAuthFilterView

import json
import shared_models.models as shared_models

from . import mixins


def ecc_delete(request, pk):
    ecc = models.EccCalibrationValue.objects.get(pk=pk)
    if utils.whales_authorized(request.user):
        ecc.delete()
        messages.success(request, _("The value curve has been successfully deleted."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse_lazy('accounts:denied_access'))


def eda_delete(request, pk):
    eda = models.EdaEquipmentAttachment.objects.get(pk=pk)
    if utils.whales_authorized(request.user):
        eda.delete()
        messages.success(request, _("The attachment has been successfully removed."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse_lazy('accounts:denied_access'))


def rst_delete(request, pk):
    rst = models.RstRecordingStage.objects.get(pk=pk)
    if utils.whales_authorized(request.user):
        rst.delete()
        messages.success(request, _("The recording stage has been successfully deleted."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse_lazy('accounts:denied_access'))


def ret_delete(request, pk):
    ret = models.RetRecordingEventType.objects.get(pk=pk)
    if utils.whales_authorized(request.user):
        ret.delete()
        messages.success(request, _("The recording Event Type has been successfully deleted."))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse_lazy('accounts:denied_access'))


class IndexView(CommonTemplateView):
    nav_menu = 'whalesdb/whale_nav_menu.html'
    site_css = 'whalesdb/whales_css.css'
    title = _("Whale Equipment Metadata Database")
    template_name = 'whalesdb/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()

        # for the most part if the user is authorized then the content is editable
        # but extending classes can choose to make content not editable even if the user is authorized
        context['auth'] = context['editable'] = utils.whales_authorized(self.request.user)

        return context


# CommonCreate Extends the UserPassesTestMixin used to determine if a user has
# has the correct privileges to interact with Creation Views
class CommonCreate(CommonAuthCreateView):

    nav_menu = 'whalesdb/whale_nav_menu.html'
    site_css = 'whalesdb/whales_css.css'
    home_url_name = "whalesdb:index"

    def get_nav_menu(self):
        if self.kwargs.get("pop"):
            return None

        return self.nav_menu

    # Upon success most creation views will be redirected to their respective 'CommonList' view. To send
    # a successful creation view somewhere else, override this method
    def get_success_url(self):
        success_url = self.success_url if self.success_url else reverse_lazy("whalesdb:list_{}".format(self.key))

        if self.kwargs.get("pop"):
            # create views intended to be pop out windows should close the window upon success
            success_url = reverse_lazy("shared_models:close_me_no_refresh")

        return success_url

    # overrides the UserPassesTestMixin test to check that a user belongs to the whalesdb_admin group
    def test_func(self):
        return self.request.user.groups.filter(name='whalesdb_admin').exists()

    # Get context returns elements used on the page. Make sure when extending to call
    # context = super().get_context_data(**kwargs) so that elements created in the parent
    # class are inherited by the extending class.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editable'] = context['auth']
        return context


class CruCreate(mixins.CruMixin, CommonCreate):
    pass


class DepCreate(mixins.DepMixin, CommonCreate):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        station_dict = [{"pk": v[0], "stn_code": v[2]} for v in
                        models.StnStation.objects.all().order_by('pk').values_list()]

        context['station_json'] = json.dumps(station_dict)
        context['java_script'] = 'whalesdb/_entry_dep_js.html'

        return context


class EccCreate(mixins.EccMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['eca'] = self.kwargs['eca']

        return initial


class EcaCreate(mixins.EcaMixin, CommonCreate):
    pass


class EdaCreate(mixins.EdaMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['dep'] = self.kwargs['dep']

        return initial


class EmmCreate(mixins.EmmMixin, CommonCreate):

    def form_valid(self, form):
        emm = form.save()

        if emm.eqt.pk == 4:
            return HttpResponseRedirect(reverse_lazy('whalesdb:details_emm', args=(emm.pk,)))
        else:
            return HttpResponseRedirect(self.get_success_url())


class EheCreate(mixins.EheMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['ecp'] = self.kwargs['ecp']

        return initial


class EqhCreate(mixins.EqhMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['emm'] = self.kwargs['pk']

        return initial


class EqoCreate(mixins.EqoMixin, CommonCreate):
    pass


class EqpCreate(mixins.EqpMixin, CommonCreate):
    pass


class EqrCreate(mixins.EqrMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['emm'] = self.kwargs['pk']

        return initial


class EtrCreate(mixins.EtrMixin, CommonCreate):
    pass


class MorCreate(mixins.MorMixin, CommonCreate):
    pass


class PrjCreate(mixins.PrjMixin, CommonCreate):
    pass


class RciCreate(mixins.RciMixin, CommonCreate):

    def get_initial(self):
        init = super().get_initial()
        if 'rec_id' in self.kwargs and models.RecDataset.objects.filter(pk=self.kwargs['rec_id']):
            init['rec_id'] = models.RecDataset.objects.get(pk=self.kwargs['rec_id'])

        return init


class RecCreate(mixins.RecMixin, CommonCreate):

    def get_initial(self):
        init = super().get_initial()
        if 'eda' in self.kwargs and models.EdaEquipmentAttachment.objects.filter(pk=self.kwargs['eda']):
            init['eda_id'] = models.EdaEquipmentAttachment.objects.get(pk=self.kwargs['eda'])

        return init

    def get_success_url(self):
        if self.kwargs.get("eda"):
            eda = models.EdaEquipmentAttachment.objects.get(pk=self.kwargs['eda'])
            return reverse_lazy("whalesdb:details_dep", args=(eda.dep.pk,))

        return super().get_success_url()


class ReeCreate(mixins.ReeMixin, CommonCreate):

    def get_initial(self):
        init = super().get_initial()
        if 'rec_id' in self.kwargs and models.RecDataset.objects.filter(pk=self.kwargs['rec_id']):
            init['rec_id'] = models.RecDataset.objects.get(pk=self.kwargs['rec_id'])

        return init


class RetCreate(mixins.RetMixin, CommonCreate):
    pass


class RscCreate(mixins.RscMixin, CommonCreate):

    def form_valid(self, form):
        obj = form.save()

        return HttpResponseRedirect(reverse_lazy("whalesdb:details_rsc", kwargs={"pk": obj.pk}))


class RstCreate(mixins.RstMixin, CommonCreate):

    def get_initial(self):
        initial = super().get_initial()
        initial['rsc'] = self.kwargs['rsc']

        return initial


class RttCreate(mixins.RttMixin, CommonCreate):
    pass


class SteCreate(mixins.SteMixin, CommonCreate):

    def get_initial(self):
        init = super().get_initial()
        if 'dep_id' in self.kwargs and models.DepDeployment.objects.filter(pk=self.kwargs['dep_id']):
            init['dep'] = models.DepDeployment.objects.get(pk=self.kwargs['dep_id'])

        if 'set_id' in self.kwargs and models.SetStationEventCode.objects.filter(pk=self.kwargs['set_id']):
            init['set_type'] = models.SetStationEventCode.objects.get(pk=self.kwargs['set_id'])
        return init


class StnCreate(mixins.StnMixin, CommonCreate):
    pass


class TeaCreate(mixins.TeaMixin, CommonCreate):
    pass


class CommonUpdate(CommonAuthUpdateView):

    nav_menu = 'whalesdb/whale_nav_menu.html'
    site_css = 'whalesdb/whales_css.css'
    home_url_name = "whalesdb:index"

    def get_success_url(self):
        success_url = self.success_url if self.success_url else reverse_lazy("whalesdb:list_{}".format(self.key))

        if self.kwargs.get("pop"):
            # create views intended to be pop out windows should close the window upon success
            success_url = reverse_lazy("shared_models:close_me_no_refresh")

        return success_url

    def get_nav_menu(self):
        if self.kwargs.get("pop"):
            return None

        return self.nav_menu

    # this function overrides UserPassesTestMixin.test_func() to determine if
    # the user should have access to this content, if the user is logged in
    # This function could be overridden in extending classes to preform further testing to see if
    # an object is editable
    def test_func(self):
        return self.request.user.groups.filter(name='whalesdb_admin').exists()

    # Get context returns elements used on the page. Make sure when extending to call
    # context = super().get_context_data(**kwargs) so that elements created in the parent
    # class are inherited by the extending class.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['editable'] = context['auth']
        return context


class CruUpdate(mixins.CruMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:details_cru", args=(self.kwargs['pk'],))


class DepUpdate(mixins.DepMixin, CommonUpdate):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        station_dict = [{"stn_id": v[0], "stn_code": v[2]} for v in
                        models.StnStation.objects.all().order_by('pk').values_list()]

        context['station_json'] = json.dumps(station_dict)
        context['java_script'] = 'whalesdb/_entry_dep_js.html'

        context['editable'] = True
        if context['auth']:
            # editable if the object has no station events
            context['editable'] = self.model.objects.get(pk=self.kwargs['pk']).station_events.count() <= 0

        return context


class EcaUpdate(mixins.EcaMixin, CommonUpdate):
    def get_success_url(self):
        return reverse_lazy("whalesdb:details_eca", args=(self.kwargs['pk'],))


class EmmUpdate(mixins.EmmMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:list_emm")


class EqhUpdate(mixins.EheMixin, CommonUpdate):
    pass


class EqhUpdate(mixins.EqhMixin, CommonUpdate):
    pass


class EqpUpdate(mixins.EqpMixin, CommonUpdate):
    def get_success_url(self):
        return reverse_lazy("whalesdb:list_eqp")


class EqrUpdate(mixins.EqrMixin, CommonUpdate):
    pass


class EtrUpdate(mixins.EtrMixin, CommonUpdate):
    def get_success_url(self):
        return reverse_lazy("whalesdb:details_etr", args=(self.kwargs['pk'],))


class MorUpdate(mixins.MorMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:list_mor")


class PrjUpdate(mixins.PrjMixin, CommonUpdate):
    def get_success_url(self):
        return reverse_lazy("whalesdb:list_prj")


class RecUpdate(mixins.RecMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:details_rec", args=(self.kwargs['pk'],))


class RetUpdate(mixins.RetMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:list_ret")


class StnUpdate(mixins.StnMixin, CommonUpdate):

    def get_success_url(self):
        return reverse_lazy("whalesdb:list_stn")


class SteUpdate(mixins.SteMixin, CommonUpdate):

    def get_initial(self):
        init = super().get_initial()
        if 'dep_id' in self.kwargs and models.DepDeployment.objects.filter(pk=self.kwargs['dep_id']):
            init['dep'] = models.DepDeployment.objects.get(pk=self.kwargs['dep_id'])

        if 'set_id' in self.kwargs and models.SetStationEventCode.objects.filter(pk=self.kwargs['set_id']):
            init['set_type'] = models.SetStationEventCode.objects.get(pk=self.kwargs['set_id'])
        return init


class CommonDetails(DetailView):
    # default template to use to create a details view
    template_name = "whalesdb/whales_details.html"

    # title to display on the list page
    title = None

    # key used for creating default list and update URLs in the get_context_data method
    key = None

    # URL linking the details page back to the proper list
    list_url = None
    update_url = None

    # By default detail objects are editable, set to false to remove update buttons
    editable = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.title:
            context['title'] = self.title

        if self.fields:
            context['fields'] = self.fields

        context['list_url'] = self.list_url if self.list_url else "whalesdb:list_{}".format(self.key)
        context['update_url'] = self.update_url if self.update_url else "whalesdb:update_{}".format(self.key)
        # for the most part if the user is authorized then the content is editable
        # but extending classes can choose to make content not editable even if the user is authorized
        context['auth'] = utils.whales_authorized(self.request.user)
        context['editable'] = context['auth'] and self.editable

        return context


class CruDetails(mixins.CruMixin, CommonDetails):
    fields = ["institute", "mission_number", "mission_name", "description", "chief_scientist", "samplers", "start_date",
              "end_date", "probe", "area_of_operation", "number_of_profiles", "meds_id", "notes", "season","vessel", ]


class DepDetails(mixins.DepMixin, CommonDetails):
    template_name = 'whalesdb/details_dep.html'
    fields = ['dep_name', 'dep_year', 'dep_month', 'stn', 'prj', 'mor']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['google_api_key'] = settings.GOOGLE_API_KEY

        context['edit_attachments'] = self.model.objects.get(pk=self.kwargs['pk']).station_events.count()
        if models.EdaEquipmentAttachment.objects.filter(dep=self.kwargs['pk']):
            edas = models.EdaEquipmentAttachment.objects.filter(dep=self.kwargs['pk'])
            for eda in edas:
                if models.RecDataset.objects.filter(eda_id=eda.pk):
                    if not hasattr(context, 'rec'):
                        context['rec'] = []

                    rec = models.RecDataset.objects.get(eda_id=eda.pk)
                    context['rec'].append({
                        'text': str(rec),
                        'id': rec.pk,
                    })

        return context


class EcaDetails(mixins.EcaMixin, CommonDetails):
    template_name = 'whalesdb/details_eca.html'
    fields = ['eca_date', 'eca_attachment', 'eca_hydrophone', 'eca_notes']


class EmmDetails(mixins.EmmMixin, CommonDetails):
    template_name = 'whalesdb/details_emm.html'
    fields = ['eqt', 'emm_make', 'emm_model', 'emm_depth_rating', 'emm_description']


class EtrDetails(mixins.EtrMixin, CommonDetails):
    fields = ['eqp', 'etr_date', 'etr_issue_desc', 'etr_repair_desc', 'etr_repaired_by', 'etr_dep_affe', 'etr_rec_affe']


class EqpDetails(mixins.EqpMixin, CommonDetails):
    template_name = "whalesdb/details_eqp.html"
    fields = ['emm', 'eqp_serial', 'eqp_asset_id', 'eqp_date_purchase', 'eqp_notes', 'eqp_retired', 'eqo_owned_by']


class MorDetails(mixins.MorMixin, CommonDetails):
    template_name = 'whalesdb/details_mor.html'
    fields = ["mor_name", "mor_max_depth", "mor_link_setup_image", "mor_additional_equipment",
              "mor_general_moor_description", "mor_notes"]
    creation_form_height = 600


class PrjDetails(mixins.PrjMixin, CommonDetails):
    fields = ['name', 'description_en', 'prj_url']
    creation_form_height = 725


class RecDetails(mixins.RecMixin, CommonDetails):
    template_name = "whalesdb/details_rec.html"
    fields = ['eda_id', 'rsc_id', 'rtt_dataset', 'rtt_in_water', 'rec_start_date', 'rec_start_time', 'rec_end_date',
              'rec_end_time', 'rec_backup_hd_1', 'rec_backup_hd_2', 'rec_notes', ]


class RscDetails(mixins.RscMixin, CommonDetails):
    template_name = "whalesdb/details_rsc.html"
    fields = ['rsc_name', 'rsc_period']
    editable = False


class RttDetails(mixins.RttMixin, CommonDetails):
    template_name = "whalesdb/details_rtt.html"
    fields = ['rtt_name', 'rtt_abb', 'rtt_period']


class StnDetails(mixins.StnMixin, CommonDetails):
    template_name = 'whalesdb/details_stn.html'
    fields = ['stn_name', 'stn_code', 'stn_revision', 'stn_planned_lat', 'stn_planned_lon',
              'stn_planned_depth', 'stn_notes']
    creation_form_height = 400

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['google_api_key'] = settings.GOOGLE_API_KEY

        return context


class CommonList(CommonAuthFilterView):

    nav_menu = 'whalesdb/whale_nav_menu.html'
    site_css = 'whalesdb/whales_css.css'
    home_url_name = "whalesdb:index"

    # fields to be used as columns to display an object in the filter view table
    fields = []

    # URL to use to create a new object to be added to the filter view
    create_url = None

    # URL to use for the details button element in the filter view's list
    details_url = None

    # URL to use for the update button element in the filter view's list
    update_url = None

    # URL to use for the delete button element in the filter view's list
    delete_url = False

    # The height of the popup dialog used to display the creation/update form
    # if not set by the extending class the default popup height will be used
    creation_form_height = None

    # By default Listed objects will have an update button, set editable to false in extending classes to disable
    editable = True

    def get_fields(self):
        if self.fields:
            return self.fields

        return ['tname|Name', 'tdescription|Description']

    def get_create_url(self):
        return self.create_url if self.create_url is not None else "whalesdb:create_{}".format(self.key)

    def get_details_url(self):
        return self.details_url if self.details_url is not None else "whalesdb:details_{}".format(self.key)

    def get_update_url(self):
        return self.update_url if self.update_url is not None else "whalesdb:update_{}".format(self.key)

    def get_delete_url(self):
        return self.delete_url if self.delete_url is not None else "whalesdb:delete_{}".format(self.key)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)

        context['fields'] = self.get_fields()

        # if the url is not None, use the value specified by the url variable.
        # if the url is None, create a url using the views key
        # this way if no URL, say details_url, is provided it's assumed the default RUL will be 'whalesdb:details_key'
        # if the details_url = False in the extending view then False will be passed to the context['detials_url']
        # variable and in the template where the variable is used for buttons and links the button and/or links can
        # be left out without causing URL Not Found issues.
        context['create_url'] = self.get_create_url()
        context['details_url'] = self.get_details_url()
        context['update_url'] = self.get_update_url()
        context['delete_url'] = self.get_delete_url()

        # for the most part if the user is authorized then the content is editable
        # but extending classes can choose to make content not editable even if the user is authorized
        context['auth'] = utils.whales_authorized(self.request.user)
        context['editable'] = context['auth'] and self.editable

        if self.creation_form_height:
            context['height'] = self.creation_form_height

        return context


class DepList(mixins.DepMixin, CommonList):
    filterset_class = filters.DepFilter
    fields = ['dep_name', 'dep_year', 'dep_month', 'stn', 'prj', 'mor']
    creation_form_height = 600

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['editable'] = False
        return context


class EcaList(mixins.EcaMixin, CommonList):
    filterset_class = filters.EcaFilter
    fields = ['eca_date', 'eca_attachment', 'eca_hydrophone']


class EmmList(mixins.EmmMixin, CommonList):
    filterset_class = filters.EmmFilter
    fields = ['eqt', 'emm_make', 'emm_model', 'emm_depth_rating']


class EqpList(mixins.EqpMixin, CommonList):
    fields = ['emm', 'eqp_serial', 'eqp_date_purchase', 'eqo_owned_by', 'eqp_retired', "eqp_deployed"]


class EtrList(mixins.EtrMixin, CommonList):
    filterset_class = filters.EtrFilter
    fields = ['etr_date', 'etr_issue_desc', 'etr_repair_desc', 'etr_repaired_by', 'etr_dep_affe', 'etr_rec_affe']


class MorList(mixins.MorMixin, CommonList):
    filterset_class = filters.MorFilter
    fields = ['mor_name', 'mor_max_depth', 'mor_notes']
    creation_form_height = 725


class PrjList(mixins.PrjMixin, CommonList):
    filterset_class = filters.PrjFilter
    creation_form_height = 400
    fields = ['tname|Name', 'tdescription|Description']


class RecList(mixins.RecMixin, CommonList):
    filterset_class = filters.RecFilter
    fields = ['eda_id', 'rsc_id', 'rec_start_date', 'rec_end_date']


class RetList(mixins.RetMixin, CommonList):
    filterset_class = filters.RetFilter
    fields = ['ret_name', 'ret_desc']

    details_url = False
    delete_url = "whalesdb:delete_ret"


class RscList(mixins.RscMixin, CommonList):
    filterset_class = filters.RscFilter
    fields = ['rsc_name', 'rsc_period']
    editable = False


class RttList(mixins.RttMixin, CommonList):
    filterset_class = filters.RttFilter
    fields = ['rtt_name', 'rtt_abb', 'rtt_offset']
    editable = False

    def get_details_url(self):
        return None


class StnList(mixins.StnMixin, CommonList):
    filterset_class = filters.StnFilter
    fields = ['stn_name', 'stn_code', 'stn_revision']


class TeaList(mixins.TeaMixin, CommonList):
    filterset_class = filters.TeaFilter
    fields = ["tea_abb", "tea_last_name", "tea_first_name"]

    details_url = False
    update_url = False


class CruList(mixins.CruMixin, CommonList):
    queryset = shared_models.Cruise.objects.all().order_by("-season", "mission_number")

    filterset_class = filters.CruFilter
    fields = ["mission_number", "description", "chief_scientist", "samplers", "start_date", "end_date", "notes",
              "season", "vessel" ]

    details_url = "whalesdb:details_cru"
    delete_url = "whalesdb:delete_cru"

    def test_func(self):
        return utils.whales_authorized(self.request.user)

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result and self.request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/denied/')
        return super().dispatch(request, *args, **kwargs)


class CruDeleteView(mixins.CruMixin, UserPassesTestMixin, DeleteView):
    success_url = reverse_lazy('whalesdb:list_cru')
    success_message = 'The cruise was successfully deleted!'
    template_name = 'whalesdb/cruise_confirm_delete.html'

    def test_func(self):
        return utils.whales_authorized(self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


