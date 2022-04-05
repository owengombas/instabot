# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = profile_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


@dataclass
class EdgeFelixVideoTimelinePageInfo:
    end_cursor: None
    has_next_page: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeFelixVideoTimelinePageInfo':
        assert isinstance(obj, dict)
        end_cursor = from_none(obj.get("end_cursor"))
        has_next_page = from_union([from_bool, from_none], obj.get("has_next_page"))
        return EdgeFelixVideoTimelinePageInfo(end_cursor, has_next_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["end_cursor"] = from_none(self.end_cursor)
        result["has_next_page"] = from_union([from_bool, from_none], self.has_next_page)
        return result


@dataclass
class EdgeFelixVideoTimelineClass:
    count: Optional[int] = None
    page_info: Optional[EdgeFelixVideoTimelinePageInfo] = None
    edges: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeFelixVideoTimelineClass':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        page_info = from_union([EdgeFelixVideoTimelinePageInfo.from_dict, from_none], obj.get("page_info"))
        edges = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("edges"))
        return EdgeFelixVideoTimelineClass(count, page_info, edges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["page_info"] = from_union([lambda x: to_class(EdgeFelixVideoTimelinePageInfo, x), from_none], self.page_info)
        result["edges"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.edges)
        return result


@dataclass
class EdgeFollowClass:
    count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeFollowClass':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        return EdgeFollowClass(count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        return result


@dataclass
class EdgeMutualFollowedBy:
    count: Optional[int] = None
    edges: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeMutualFollowedBy':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        edges = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("edges"))
        return EdgeMutualFollowedBy(count, edges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["edges"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.edges)
        return result


@dataclass
class Dimensions:
    height: Optional[int] = None
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Dimensions':
        assert isinstance(obj, dict)
        height = from_union([from_int, from_none], obj.get("height"))
        width = from_union([from_int, from_none], obj.get("width"))
        return Dimensions(height, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["height"] = from_union([from_int, from_none], self.height)
        result["width"] = from_union([from_int, from_none], self.width)
        return result


@dataclass
class EdgeMediaTo:
    edges: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeMediaTo':
        assert isinstance(obj, dict)
        edges = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("edges"))
        return EdgeMediaTo(edges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["edges"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.edges)
        return result


@dataclass
class Owner:
    id: Optional[str] = None
    username: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Owner':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        username = from_union([from_str, from_none], obj.get("username"))
        return Owner(id, username)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["username"] = from_union([from_str, from_none], self.username)
        return result


@dataclass
class SharingFrictionInfo:
    bloks_app_url: None
    should_have_sharing_friction: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SharingFrictionInfo':
        assert isinstance(obj, dict)
        bloks_app_url = from_none(obj.get("bloks_app_url"))
        should_have_sharing_friction = from_union([from_bool, from_none], obj.get("should_have_sharing_friction"))
        return SharingFrictionInfo(bloks_app_url, should_have_sharing_friction)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bloks_app_url"] = from_none(self.bloks_app_url)
        result["should_have_sharing_friction"] = from_union([from_bool, from_none], self.should_have_sharing_friction)
        return result


@dataclass
class FluffyNode:
    fact_check_overall_rating: None
    fact_check_information: None
    gating_info: None
    media_overlay_info: None
    typename: Optional[str] = None
    id: Optional[str] = None
    shortcode: Optional[str] = None
    dimensions: Optional[Dimensions] = None
    display_url: Optional[str] = None
    edge_media_to_tagged_user: Optional[EdgeMediaTo] = None
    sharing_friction_info: Optional[SharingFrictionInfo] = None
    media_preview: Optional[str] = None
    owner: Optional[Owner] = None
    is_video: Optional[bool] = None
    has_upcoming_event: Optional[bool] = None
    accessibility_caption: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyNode':
        assert isinstance(obj, dict)
        fact_check_overall_rating = from_none(obj.get("fact_check_overall_rating"))
        fact_check_information = from_none(obj.get("fact_check_information"))
        gating_info = from_none(obj.get("gating_info"))
        media_overlay_info = from_none(obj.get("media_overlay_info"))
        typename = from_union([from_str, from_none], obj.get("__typename"))
        id = from_union([from_str, from_none], obj.get("id"))
        shortcode = from_union([from_str, from_none], obj.get("shortcode"))
        dimensions = from_union([Dimensions.from_dict, from_none], obj.get("dimensions"))
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        edge_media_to_tagged_user = from_union([EdgeMediaTo.from_dict, from_none], obj.get("edge_media_to_tagged_user"))
        sharing_friction_info = from_union([SharingFrictionInfo.from_dict, from_none], obj.get("sharing_friction_info"))
        media_preview = from_union([from_str, from_none], obj.get("media_preview"))
        owner = from_union([Owner.from_dict, from_none], obj.get("owner"))
        is_video = from_union([from_bool, from_none], obj.get("is_video"))
        has_upcoming_event = from_union([from_bool, from_none], obj.get("has_upcoming_event"))
        accessibility_caption = from_union([from_str, from_none], obj.get("accessibility_caption"))
        return FluffyNode(fact_check_overall_rating, fact_check_information, gating_info, media_overlay_info, typename, id, shortcode, dimensions, display_url, edge_media_to_tagged_user, sharing_friction_info, media_preview, owner, is_video, has_upcoming_event, accessibility_caption)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fact_check_overall_rating"] = from_none(self.fact_check_overall_rating)
        result["fact_check_information"] = from_none(self.fact_check_information)
        result["gating_info"] = from_none(self.gating_info)
        result["media_overlay_info"] = from_none(self.media_overlay_info)
        result["__typename"] = from_union([from_str, from_none], self.typename)
        result["id"] = from_union([from_str, from_none], self.id)
        result["shortcode"] = from_union([from_str, from_none], self.shortcode)
        result["dimensions"] = from_union([lambda x: to_class(Dimensions, x), from_none], self.dimensions)
        result["display_url"] = from_union([from_str, from_none], self.display_url)
        result["edge_media_to_tagged_user"] = from_union([lambda x: to_class(EdgeMediaTo, x), from_none], self.edge_media_to_tagged_user)
        result["sharing_friction_info"] = from_union([lambda x: to_class(SharingFrictionInfo, x), from_none], self.sharing_friction_info)
        result["media_preview"] = from_union([from_str, from_none], self.media_preview)
        result["owner"] = from_union([lambda x: to_class(Owner, x), from_none], self.owner)
        result["is_video"] = from_union([from_bool, from_none], self.is_video)
        result["has_upcoming_event"] = from_union([from_bool, from_none], self.has_upcoming_event)
        result["accessibility_caption"] = from_union([from_str, from_none], self.accessibility_caption)
        return result


@dataclass
class EdgeSidecarToChildrenEdge:
    node: Optional[FluffyNode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeSidecarToChildrenEdge':
        assert isinstance(obj, dict)
        node = from_union([FluffyNode.from_dict, from_none], obj.get("node"))
        return EdgeSidecarToChildrenEdge(node)

    def to_dict(self) -> dict:
        result: dict = {}
        result["node"] = from_union([lambda x: to_class(FluffyNode, x), from_none], self.node)
        return result


@dataclass
class EdgeSidecarToChildren:
    edges: Optional[List[EdgeSidecarToChildrenEdge]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeSidecarToChildren':
        assert isinstance(obj, dict)
        edges = from_union([lambda x: from_list(EdgeSidecarToChildrenEdge.from_dict, x), from_none], obj.get("edges"))
        return EdgeSidecarToChildren(edges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["edges"] = from_union([lambda x: from_list(lambda x: to_class(EdgeSidecarToChildrenEdge, x), x), from_none], self.edges)
        return result


@dataclass
class ThumbnailResource:
    src: Optional[str] = None
    config_width: Optional[int] = None
    config_height: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ThumbnailResource':
        assert isinstance(obj, dict)
        src = from_union([from_str, from_none], obj.get("src"))
        config_width = from_union([from_int, from_none], obj.get("config_width"))
        config_height = from_union([from_int, from_none], obj.get("config_height"))
        return ThumbnailResource(src, config_width, config_height)

    def to_dict(self) -> dict:
        result: dict = {}
        result["src"] = from_union([from_str, from_none], self.src)
        result["config_width"] = from_union([from_int, from_none], self.config_width)
        result["config_height"] = from_union([from_int, from_none], self.config_height)
        return result


@dataclass
class PurpleNode:
    fact_check_overall_rating: None
    fact_check_information: None
    gating_info: None
    media_overlay_info: None
    location: None
    typename: Optional[str] = None
    id: Optional[str] = None
    shortcode: Optional[str] = None
    dimensions: Optional[Dimensions] = None
    display_url: Optional[str] = None
    edge_media_to_tagged_user: Optional[EdgeMediaTo] = None
    sharing_friction_info: Optional[SharingFrictionInfo] = None
    media_preview: Optional[str] = None
    owner: Optional[Owner] = None
    is_video: Optional[bool] = None
    has_upcoming_event: Optional[bool] = None
    accessibility_caption: Optional[str] = None
    edge_media_to_caption: Optional[EdgeMediaTo] = None
    edge_media_to_comment: Optional[EdgeFollowClass] = None
    comments_disabled: Optional[bool] = None
    taken_at_timestamp: Optional[int] = None
    edge_liked_by: Optional[EdgeFollowClass] = None
    edge_media_preview_like: Optional[EdgeFollowClass] = None
    thumbnail_src: Optional[str] = None
    thumbnail_resources: Optional[List[ThumbnailResource]] = None
    coauthor_producers: Optional[List[Any]] = None
    pinned_for_users: Optional[List[Any]] = None
    edge_sidecar_to_children: Optional[EdgeSidecarToChildren] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleNode':
        assert isinstance(obj, dict)
        fact_check_overall_rating = from_none(obj.get("fact_check_overall_rating"))
        fact_check_information = from_none(obj.get("fact_check_information"))
        gating_info = from_none(obj.get("gating_info"))
        media_overlay_info = from_none(obj.get("media_overlay_info"))
        location = from_none(obj.get("location"))
        typename = from_union([from_str, from_none], obj.get("__typename"))
        id = from_union([from_str, from_none], obj.get("id"))
        shortcode = from_union([from_str, from_none], obj.get("shortcode"))
        dimensions = from_union([Dimensions.from_dict, from_none], obj.get("dimensions"))
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        edge_media_to_tagged_user = from_union([EdgeMediaTo.from_dict, from_none], obj.get("edge_media_to_tagged_user"))
        sharing_friction_info = from_union([SharingFrictionInfo.from_dict, from_none], obj.get("sharing_friction_info"))
        media_preview = from_union([from_none, from_str], obj.get("media_preview"))
        owner = from_union([Owner.from_dict, from_none], obj.get("owner"))
        is_video = from_union([from_bool, from_none], obj.get("is_video"))
        has_upcoming_event = from_union([from_bool, from_none], obj.get("has_upcoming_event"))
        accessibility_caption = from_union([from_str, from_none], obj.get("accessibility_caption"))
        edge_media_to_caption = from_union([EdgeMediaTo.from_dict, from_none], obj.get("edge_media_to_caption"))
        edge_media_to_comment = from_union([EdgeFollowClass.from_dict, from_none], obj.get("edge_media_to_comment"))
        comments_disabled = from_union([from_bool, from_none], obj.get("comments_disabled"))
        taken_at_timestamp = from_union([from_int, from_none], obj.get("taken_at_timestamp"))
        edge_liked_by = from_union([EdgeFollowClass.from_dict, from_none], obj.get("edge_liked_by"))
        edge_media_preview_like = from_union([EdgeFollowClass.from_dict, from_none], obj.get("edge_media_preview_like"))
        thumbnail_src = from_union([from_str, from_none], obj.get("thumbnail_src"))
        thumbnail_resources = from_union([lambda x: from_list(ThumbnailResource.from_dict, x), from_none], obj.get("thumbnail_resources"))
        coauthor_producers = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("coauthor_producers"))
        pinned_for_users = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pinned_for_users"))
        edge_sidecar_to_children = from_union([EdgeSidecarToChildren.from_dict, from_none], obj.get("edge_sidecar_to_children"))
        return PurpleNode(fact_check_overall_rating, fact_check_information, gating_info, media_overlay_info, location, typename, id, shortcode, dimensions, display_url, edge_media_to_tagged_user, sharing_friction_info, media_preview, owner, is_video, has_upcoming_event, accessibility_caption, edge_media_to_caption, edge_media_to_comment, comments_disabled, taken_at_timestamp, edge_liked_by, edge_media_preview_like, thumbnail_src, thumbnail_resources, coauthor_producers, pinned_for_users, edge_sidecar_to_children)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fact_check_overall_rating"] = from_none(self.fact_check_overall_rating)
        result["fact_check_information"] = from_none(self.fact_check_information)
        result["gating_info"] = from_none(self.gating_info)
        result["media_overlay_info"] = from_none(self.media_overlay_info)
        result["location"] = from_none(self.location)
        result["__typename"] = from_union([from_str, from_none], self.typename)
        result["id"] = from_union([from_str, from_none], self.id)
        result["shortcode"] = from_union([from_str, from_none], self.shortcode)
        result["dimensions"] = from_union([lambda x: to_class(Dimensions, x), from_none], self.dimensions)
        result["display_url"] = from_union([from_str, from_none], self.display_url)
        result["edge_media_to_tagged_user"] = from_union([lambda x: to_class(EdgeMediaTo, x), from_none], self.edge_media_to_tagged_user)
        result["sharing_friction_info"] = from_union([lambda x: to_class(SharingFrictionInfo, x), from_none], self.sharing_friction_info)
        result["media_preview"] = from_union([from_none, from_str], self.media_preview)
        result["owner"] = from_union([lambda x: to_class(Owner, x), from_none], self.owner)
        result["is_video"] = from_union([from_bool, from_none], self.is_video)
        result["has_upcoming_event"] = from_union([from_bool, from_none], self.has_upcoming_event)
        result["accessibility_caption"] = from_union([from_str, from_none], self.accessibility_caption)
        result["edge_media_to_caption"] = from_union([lambda x: to_class(EdgeMediaTo, x), from_none], self.edge_media_to_caption)
        result["edge_media_to_comment"] = from_union([lambda x: to_class(EdgeFollowClass, x), from_none], self.edge_media_to_comment)
        result["comments_disabled"] = from_union([from_bool, from_none], self.comments_disabled)
        result["taken_at_timestamp"] = from_union([from_int, from_none], self.taken_at_timestamp)
        result["edge_liked_by"] = from_union([lambda x: to_class(EdgeFollowClass, x), from_none], self.edge_liked_by)
        result["edge_media_preview_like"] = from_union([lambda x: to_class(EdgeFollowClass, x), from_none], self.edge_media_preview_like)
        result["thumbnail_src"] = from_union([from_str, from_none], self.thumbnail_src)
        result["thumbnail_resources"] = from_union([lambda x: from_list(lambda x: to_class(ThumbnailResource, x), x), from_none], self.thumbnail_resources)
        result["coauthor_producers"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.coauthor_producers)
        result["pinned_for_users"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pinned_for_users)
        result["edge_sidecar_to_children"] = from_union([lambda x: to_class(EdgeSidecarToChildren, x), from_none], self.edge_sidecar_to_children)
        return result


@dataclass
class EdgeOwnerToTimelineMediaEdge:
    node: Optional[PurpleNode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeOwnerToTimelineMediaEdge':
        assert isinstance(obj, dict)
        node = from_union([PurpleNode.from_dict, from_none], obj.get("node"))
        return EdgeOwnerToTimelineMediaEdge(node)

    def to_dict(self) -> dict:
        result: dict = {}
        result["node"] = from_union([lambda x: to_class(PurpleNode, x), from_none], self.node)
        return result


@dataclass
class EdgeOwnerToTimelineMediaPageInfo:
    has_next_page: Optional[bool] = None
    end_cursor: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeOwnerToTimelineMediaPageInfo':
        assert isinstance(obj, dict)
        has_next_page = from_union([from_bool, from_none], obj.get("has_next_page"))
        end_cursor = from_union([from_str, from_none], obj.get("end_cursor"))
        return EdgeOwnerToTimelineMediaPageInfo(has_next_page, end_cursor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["has_next_page"] = from_union([from_bool, from_none], self.has_next_page)
        result["end_cursor"] = from_union([from_str, from_none], self.end_cursor)
        return result


@dataclass
class EdgeOwnerToTimelineMedia:
    count: Optional[int] = None
    page_info: Optional[EdgeOwnerToTimelineMediaPageInfo] = None
    edges: Optional[List[EdgeOwnerToTimelineMediaEdge]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EdgeOwnerToTimelineMedia':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        page_info = from_union([EdgeOwnerToTimelineMediaPageInfo.from_dict, from_none], obj.get("page_info"))
        edges = from_union([lambda x: from_list(EdgeOwnerToTimelineMediaEdge.from_dict, x), from_none], obj.get("edges"))
        return EdgeOwnerToTimelineMedia(count, page_info, edges)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["page_info"] = from_union([lambda x: to_class(EdgeOwnerToTimelineMediaPageInfo, x), from_none], self.page_info)
        result["edges"] = from_union([lambda x: from_list(lambda x: to_class(EdgeOwnerToTimelineMediaEdge, x), x), from_none], self.edges)
        return result


@dataclass
class User:
    external_url: None
    external_url_linkshimmed: None
    business_address_json: None
    business_email: None
    business_phone_number: None
    business_category_name: None
    overall_category_name: None
    category_enum: None
    state_controlled_media_country: None
    connected_fb_page: None
    biography: Optional[str] = None
    blocked_by_viewer: Optional[bool] = None
    restricted_by_viewer: Optional[bool] = None
    country_block: Optional[bool] = None
    edge_followed_by: Optional[EdgeFollowClass] = None
    fbid: Optional[str] = None
    followed_by_viewer: Optional[bool] = None
    edge_follow: Optional[EdgeFollowClass] = None
    follows_viewer: Optional[bool] = None
    full_name: Optional[str] = None
    has_ar_effects: Optional[bool] = None
    has_clips: Optional[bool] = None
    has_guides: Optional[bool] = None
    has_channel: Optional[bool] = None
    has_blocked_viewer: Optional[bool] = None
    highlight_reel_count: Optional[int] = None
    has_requested_viewer: Optional[bool] = None
    hide_like_and_view_counts: Optional[bool] = None
    id: Optional[str] = None
    is_business_account: Optional[bool] = None
    is_professional_account: Optional[bool] = None
    is_supervision_enabled: Optional[bool] = None
    is_guardian_of_viewer: Optional[bool] = None
    is_supervised_by_viewer: Optional[bool] = None
    is_embeds_disabled: Optional[bool] = None
    is_joined_recently: Optional[bool] = None
    business_contact_method: Optional[str] = None
    category_name: Optional[str] = None
    is_private: Optional[bool] = None
    is_verified: Optional[bool] = None
    edge_mutual_followed_by: Optional[EdgeMutualFollowedBy] = None
    profile_pic_url: Optional[str] = None
    profile_pic_url_hd: Optional[str] = None
    requested_by_viewer: Optional[bool] = None
    should_show_category: Optional[bool] = None
    should_show_public_contacts: Optional[bool] = None
    username: Optional[str] = None
    pronouns: Optional[List[Any]] = None
    edge_felix_video_timeline: Optional[EdgeFelixVideoTimelineClass] = None
    edge_owner_to_timeline_media: Optional[EdgeOwnerToTimelineMedia] = None
    edge_saved_media: Optional[EdgeFelixVideoTimelineClass] = None
    edge_media_collections: Optional[EdgeFelixVideoTimelineClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        external_url = from_none(obj.get("external_url"))
        external_url_linkshimmed = from_none(obj.get("external_url_linkshimmed"))
        business_address_json = from_none(obj.get("business_address_json"))
        business_email = from_none(obj.get("business_email"))
        business_phone_number = from_none(obj.get("business_phone_number"))
        business_category_name = from_none(obj.get("business_category_name"))
        overall_category_name = from_none(obj.get("overall_category_name"))
        category_enum = from_none(obj.get("category_enum"))
        state_controlled_media_country = from_none(obj.get("state_controlled_media_country"))
        connected_fb_page = from_none(obj.get("connected_fb_page"))
        biography = from_union([from_str, from_none], obj.get("biography"))
        blocked_by_viewer = from_union([from_bool, from_none], obj.get("blocked_by_viewer"))
        restricted_by_viewer = from_union([from_bool, from_none], obj.get("restricted_by_viewer"))
        country_block = from_union([from_bool, from_none], obj.get("country_block"))
        edge_followed_by = from_union([EdgeFollowClass.from_dict, from_none], obj.get("edge_followed_by"))
        fbid = from_union([from_str, from_none], obj.get("fbid"))
        followed_by_viewer = from_union([from_bool, from_none], obj.get("followed_by_viewer"))
        edge_follow = from_union([EdgeFollowClass.from_dict, from_none], obj.get("edge_follow"))
        follows_viewer = from_union([from_bool, from_none], obj.get("follows_viewer"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        has_ar_effects = from_union([from_bool, from_none], obj.get("has_ar_effects"))
        has_clips = from_union([from_bool, from_none], obj.get("has_clips"))
        has_guides = from_union([from_bool, from_none], obj.get("has_guides"))
        has_channel = from_union([from_bool, from_none], obj.get("has_channel"))
        has_blocked_viewer = from_union([from_bool, from_none], obj.get("has_blocked_viewer"))
        highlight_reel_count = from_union([from_int, from_none], obj.get("highlight_reel_count"))
        has_requested_viewer = from_union([from_bool, from_none], obj.get("has_requested_viewer"))
        hide_like_and_view_counts = from_union([from_bool, from_none], obj.get("hide_like_and_view_counts"))
        id = from_union([from_str, from_none], obj.get("id"))
        is_business_account = from_union([from_bool, from_none], obj.get("is_business_account"))
        is_professional_account = from_union([from_bool, from_none], obj.get("is_professional_account"))
        is_supervision_enabled = from_union([from_bool, from_none], obj.get("is_supervision_enabled"))
        is_guardian_of_viewer = from_union([from_bool, from_none], obj.get("is_guardian_of_viewer"))
        is_supervised_by_viewer = from_union([from_bool, from_none], obj.get("is_supervised_by_viewer"))
        is_embeds_disabled = from_union([from_bool, from_none], obj.get("is_embeds_disabled"))
        is_joined_recently = from_union([from_bool, from_none], obj.get("is_joined_recently"))
        business_contact_method = from_union([from_str, from_none], obj.get("business_contact_method"))
        category_name = from_union([from_str, from_none], obj.get("category_name"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        edge_mutual_followed_by = from_union([EdgeMutualFollowedBy.from_dict, from_none], obj.get("edge_mutual_followed_by"))
        profile_pic_url = from_union([from_str, from_none], obj.get("profile_pic_url"))
        profile_pic_url_hd = from_union([from_str, from_none], obj.get("profile_pic_url_hd"))
        requested_by_viewer = from_union([from_bool, from_none], obj.get("requested_by_viewer"))
        should_show_category = from_union([from_bool, from_none], obj.get("should_show_category"))
        should_show_public_contacts = from_union([from_bool, from_none], obj.get("should_show_public_contacts"))
        username = from_union([from_str, from_none], obj.get("username"))
        pronouns = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("pronouns"))
        edge_felix_video_timeline = from_union([EdgeFelixVideoTimelineClass.from_dict, from_none], obj.get("edge_felix_video_timeline"))
        edge_owner_to_timeline_media = from_union([EdgeOwnerToTimelineMedia.from_dict, from_none], obj.get("edge_owner_to_timeline_media"))
        edge_saved_media = from_union([EdgeFelixVideoTimelineClass.from_dict, from_none], obj.get("edge_saved_media"))
        edge_media_collections = from_union([EdgeFelixVideoTimelineClass.from_dict, from_none], obj.get("edge_media_collections"))
        return User(external_url, external_url_linkshimmed, business_address_json, business_email, business_phone_number, business_category_name, overall_category_name, category_enum, state_controlled_media_country, connected_fb_page, biography, blocked_by_viewer, restricted_by_viewer, country_block, edge_followed_by, fbid, followed_by_viewer, edge_follow, follows_viewer, full_name, has_ar_effects, has_clips, has_guides, has_channel, has_blocked_viewer, highlight_reel_count, has_requested_viewer, hide_like_and_view_counts, id, is_business_account, is_professional_account, is_supervision_enabled, is_guardian_of_viewer, is_supervised_by_viewer, is_embeds_disabled, is_joined_recently, business_contact_method, category_name, is_private, is_verified, edge_mutual_followed_by, profile_pic_url, profile_pic_url_hd, requested_by_viewer, should_show_category, should_show_public_contacts, username, pronouns, edge_felix_video_timeline, edge_owner_to_timeline_media, edge_saved_media, edge_media_collections)

    def to_dict(self) -> dict:
        result: dict = {}
        result["external_url"] = from_none(self.external_url)
        result["external_url_linkshimmed"] = from_none(self.external_url_linkshimmed)
        result["business_address_json"] = from_none(self.business_address_json)
        result["business_email"] = from_none(self.business_email)
        result["business_phone_number"] = from_none(self.business_phone_number)
        result["business_category_name"] = from_none(self.business_category_name)
        result["overall_category_name"] = from_none(self.overall_category_name)
        result["category_enum"] = from_none(self.category_enum)
        result["state_controlled_media_country"] = from_none(self.state_controlled_media_country)
        result["connected_fb_page"] = from_none(self.connected_fb_page)
        result["biography"] = from_union([from_str, from_none], self.biography)
        result["blocked_by_viewer"] = from_union([from_bool, from_none], self.blocked_by_viewer)
        result["restricted_by_viewer"] = from_union([from_bool, from_none], self.restricted_by_viewer)
        result["country_block"] = from_union([from_bool, from_none], self.country_block)
        result["edge_followed_by"] = from_union([lambda x: to_class(EdgeFollowClass, x), from_none], self.edge_followed_by)
        result["fbid"] = from_union([from_str, from_none], self.fbid)
        result["followed_by_viewer"] = from_union([from_bool, from_none], self.followed_by_viewer)
        result["edge_follow"] = from_union([lambda x: to_class(EdgeFollowClass, x), from_none], self.edge_follow)
        result["follows_viewer"] = from_union([from_bool, from_none], self.follows_viewer)
        result["full_name"] = from_union([from_str, from_none], self.full_name)
        result["has_ar_effects"] = from_union([from_bool, from_none], self.has_ar_effects)
        result["has_clips"] = from_union([from_bool, from_none], self.has_clips)
        result["has_guides"] = from_union([from_bool, from_none], self.has_guides)
        result["has_channel"] = from_union([from_bool, from_none], self.has_channel)
        result["has_blocked_viewer"] = from_union([from_bool, from_none], self.has_blocked_viewer)
        result["highlight_reel_count"] = from_union([from_int, from_none], self.highlight_reel_count)
        result["has_requested_viewer"] = from_union([from_bool, from_none], self.has_requested_viewer)
        result["hide_like_and_view_counts"] = from_union([from_bool, from_none], self.hide_like_and_view_counts)
        result["id"] = from_union([from_str, from_none], self.id)
        result["is_business_account"] = from_union([from_bool, from_none], self.is_business_account)
        result["is_professional_account"] = from_union([from_bool, from_none], self.is_professional_account)
        result["is_supervision_enabled"] = from_union([from_bool, from_none], self.is_supervision_enabled)
        result["is_guardian_of_viewer"] = from_union([from_bool, from_none], self.is_guardian_of_viewer)
        result["is_supervised_by_viewer"] = from_union([from_bool, from_none], self.is_supervised_by_viewer)
        result["is_embeds_disabled"] = from_union([from_bool, from_none], self.is_embeds_disabled)
        result["is_joined_recently"] = from_union([from_bool, from_none], self.is_joined_recently)
        result["business_contact_method"] = from_union([from_str, from_none], self.business_contact_method)
        result["category_name"] = from_union([from_str, from_none], self.category_name)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["edge_mutual_followed_by"] = from_union([lambda x: to_class(EdgeMutualFollowedBy, x), from_none], self.edge_mutual_followed_by)
        result["profile_pic_url"] = from_union([from_str, from_none], self.profile_pic_url)
        result["profile_pic_url_hd"] = from_union([from_str, from_none], self.profile_pic_url_hd)
        result["requested_by_viewer"] = from_union([from_bool, from_none], self.requested_by_viewer)
        result["should_show_category"] = from_union([from_bool, from_none], self.should_show_category)
        result["should_show_public_contacts"] = from_union([from_bool, from_none], self.should_show_public_contacts)
        result["username"] = from_union([from_str, from_none], self.username)
        result["pronouns"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.pronouns)
        result["edge_felix_video_timeline"] = from_union([lambda x: to_class(EdgeFelixVideoTimelineClass, x), from_none], self.edge_felix_video_timeline)
        result["edge_owner_to_timeline_media"] = from_union([lambda x: to_class(EdgeOwnerToTimelineMedia, x), from_none], self.edge_owner_to_timeline_media)
        result["edge_saved_media"] = from_union([lambda x: to_class(EdgeFelixVideoTimelineClass, x), from_none], self.edge_saved_media)
        result["edge_media_collections"] = from_union([lambda x: to_class(EdgeFelixVideoTimelineClass, x), from_none], self.edge_media_collections)
        return result


@dataclass
class Graphql:
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Graphql':
        assert isinstance(obj, dict)
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Graphql(user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class ProfileResponse:
    toast_content_on_load: None
    seo_category_infos: Optional[List[List[str]]] = None
    logging_page_id: Optional[str] = None
    show_suggested_profiles: Optional[bool] = None
    graphql: Optional[Graphql] = None
    show_qr_modal: Optional[bool] = None
    show_view_shop: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ProfileResponse':
        assert isinstance(obj, dict)
        toast_content_on_load = from_none(obj.get("toast_content_on_load"))
        seo_category_infos = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("seo_category_infos"))
        logging_page_id = from_union([from_str, from_none], obj.get("logging_page_id"))
        show_suggested_profiles = from_union([from_bool, from_none], obj.get("show_suggested_profiles"))
        graphql = from_union([Graphql.from_dict, from_none], obj.get("graphql"))
        show_qr_modal = from_union([from_bool, from_none], obj.get("show_qr_modal"))
        show_view_shop = from_union([from_bool, from_none], obj.get("show_view_shop"))
        return ProfileResponse(toast_content_on_load, seo_category_infos, logging_page_id, show_suggested_profiles, graphql, show_qr_modal, show_view_shop)

    def to_dict(self) -> dict:
        result: dict = {}
        result["toast_content_on_load"] = from_none(self.toast_content_on_load)
        result["seo_category_infos"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.seo_category_infos)
        result["logging_page_id"] = from_union([from_str, from_none], self.logging_page_id)
        result["show_suggested_profiles"] = from_union([from_bool, from_none], self.show_suggested_profiles)
        result["graphql"] = from_union([lambda x: to_class(Graphql, x), from_none], self.graphql)
        result["show_qr_modal"] = from_union([from_bool, from_none], self.show_qr_modal)
        result["show_view_shop"] = from_union([from_bool, from_none], self.show_view_shop)
        return result


def profile_response_from_dict(s: Any) -> ProfileResponse:
    return ProfileResponse.from_dict(s)


def profile_response_to_dict(x: ProfileResponse) -> Any:
    return to_class(ProfileResponse, x)
