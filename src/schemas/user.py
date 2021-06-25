import graphene
from graphql import GraphQLError
from serializers.user import UserGrapheneModel, UserGrapheneInputModel
from models.user import User as UserModel


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserGrapheneModel)
    user = graphene.Field(UserGrapheneModel, id=graphene.NonNull(graphene.Int))

    async def resolve_users(self, info):
        return list(UserModel.objects.all())

    async def resolve_user(self, info, id):
        if id is None:
            raise GraphQLError('ID not provided')
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            raise GraphQLError('Entity not found')


class CreateUser(graphene.Mutation):
    class Arguments:
        user_input = UserGrapheneInputModel()

    user = graphene.Field(lambda: UserGrapheneModel)

    @staticmethod
    async def mutate(parent, info, user_input):
        user = UserModel(**user_input)
        user.save()
        return CreateUser(user=user)


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class UserSubscription(graphene.ObjectType):
    count = graphene.Int(upto=graphene.Int())

    @staticmethod
    async def subscribe_count(root, info, upto=3):
        for i in range(upto):
            yield i
            await asyncio.sleep(1)
