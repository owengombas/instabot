# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = followers_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class Interventions:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Interventions':
        assert isinstance(obj, dict)
        return Interventions()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class GrowthFrictionInfo:
    has_active_interventions: Optional[bool] = None
    interventions: Optional[Interventions] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GrowthFrictionInfo':
        assert isinstance(obj, dict)
        has_active_interventions = from_union([from_bool, from_none], obj.get("has_active_interventions"))
        interventions = from_union([Interventions.from_dict, from_none], obj.get("interventions"))
        return GrowthFrictionInfo(has_active_interventions, interventions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["has_active_interventions"] = from_union([from_bool, from_none], self.has_active_interventions)
        result["interventions"] = from_union([lambda x: to_class(Interventions, x), from_none], self.interventions)
        return result


@dataclass
class User:
    pk: Optional[int] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    is_private: Optional[bool] = None
    profile_pic_url: Optional[str] = None
    profile_pic_id: Optional[str] = None
    is_verified: Optional[bool] = None
    follow_friction_type: Optional[int] = None
    growth_friction_info: Optional[GrowthFrictionInfo] = None
    account_badges: Optional[List[Any]] = None
    has_anonymous_profile_picture: Optional[bool] = None
    has_highlight_reels: Optional[bool] = None
    has_primary_country_in_feed: Optional[bool] = None
    has_primary_country_in_profile: Optional[bool] = None
    transparency_product_enabled: Optional[bool] = None
    latest_reel_media: Optional[int] = None
    is_favorite: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        pk = from_union([from_int, from_none], obj.get("pk"))
        username = from_union([from_str, from_none], obj.get("username"))
        full_name = from_union([from_str, from_none], obj.get("full_name"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        profile_pic_url = from_union([from_str, from_none], obj.get("profile_pic_url"))
        profile_pic_id = from_union([from_str, from_none], obj.get("profile_pic_id"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        follow_friction_type = from_union([from_int, from_none], obj.get("follow_friction_type"))
        growth_friction_info = from_union([GrowthFrictionInfo.from_dict, from_none], obj.get("growth_friction_info"))
        account_badges = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("account_badges"))
        has_anonymous_profile_picture = from_union([from_bool, from_none], obj.get("has_anonymous_profile_picture"))
        has_highlight_reels = from_union([from_bool, from_none], obj.get("has_highlight_reels"))
        has_primary_country_in_feed = from_union([from_bool, from_none], obj.get("has_primary_country_in_feed"))
        has_primary_country_in_profile = from_union([from_bool, from_none], obj.get("has_primary_country_in_profile"))
        transparency_product_enabled = from_union([from_bool, from_none], obj.get("transparency_product_enabled"))
        latest_reel_media = from_union([from_int, from_none], obj.get("latest_reel_media"))
        is_favorite = from_union([from_bool, from_none], obj.get("is_favorite"))
        return User(pk, username, full_name, is_private, profile_pic_url, profile_pic_id, is_verified, follow_friction_type, growth_friction_info, account_badges, has_anonymous_profile_picture, has_highlight_reels, has_primary_country_in_feed, has_primary_country_in_profile, transparency_product_enabled, latest_reel_media, is_favorite)

    def to_dict(self) -> dict:
        result: dict = {}
        result["pk"] = from_union([from_int, from_none], self.pk)
        result["username"] = from_union([from_str, from_none], self.username)
        result["full_name"] = from_union([from_str, from_none], self.full_name)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["profile_pic_url"] = from_union([from_str, from_none], self.profile_pic_url)
        result["profile_pic_id"] = from_union([from_str, from_none], self.profile_pic_id)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["follow_friction_type"] = from_union([from_int, from_none], self.follow_friction_type)
        result["growth_friction_info"] = from_union([lambda x: to_class(GrowthFrictionInfo, x), from_none], self.growth_friction_info)
        result["account_badges"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.account_badges)
        result["has_anonymous_profile_picture"] = from_union([from_bool, from_none], self.has_anonymous_profile_picture)
        result["has_highlight_reels"] = from_union([from_bool, from_none], self.has_highlight_reels)
        result["has_primary_country_in_feed"] = from_union([from_bool, from_none], self.has_primary_country_in_feed)
        result["has_primary_country_in_profile"] = from_union([from_bool, from_none], self.has_primary_country_in_profile)
        result["transparency_product_enabled"] = from_union([from_bool, from_none], self.transparency_product_enabled)
        result["latest_reel_media"] = from_union([from_int, from_none], self.latest_reel_media)
        result["is_favorite"] = from_union([from_bool, from_none], self.is_favorite)
        return result


@dataclass
class FollowersResponse:
    next_max_id: Optional[int] = None
    users: Optional[List[User]] = None
    big_list: Optional[bool] = None
    page_size: Optional[int] = None
    should_limit_list_of_followers: Optional[bool] = None
    status: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FollowersResponse':
        assert isinstance(obj, dict)
        next_max_id = from_union([from_none, lambda x: int(from_str(x))], obj.get("next_max_id"))
        users = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("users"))
        big_list = from_union([from_bool, from_none], obj.get("big_list"))
        page_size = from_union([from_int, from_none], obj.get("page_size"))
        should_limit_list_of_followers = from_union([from_bool, from_none], obj.get("should_limit_list_of_followers"))
        status = from_union([from_str, from_none], obj.get("status"))
        return FollowersResponse(next_max_id, users, big_list, page_size, should_limit_list_of_followers, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_max_id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.next_max_id)
        result["users"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none], self.users)
        result["big_list"] = from_union([from_bool, from_none], self.big_list)
        result["page_size"] = from_union([from_int, from_none], self.page_size)
        result["should_limit_list_of_followers"] = from_union([from_bool, from_none], self.should_limit_list_of_followers)
        result["status"] = from_union([from_str, from_none], self.status)
        return result


def followers_response_from_dict(s: Any) -> FollowersResponse:
    return FollowersResponse.from_dict(s)


def followers_response_to_dict(x: FollowersResponse) -> Any:
    return to_class(FollowersResponse, x)
