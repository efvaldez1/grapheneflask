import graphene
from graphene import relay
from graphe_sqlachemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from models import db_session, Category as CategoryModel,Product as ProductModel

class Category(SQLAlchemyObjectType):
	class Meta:
		model = CategoryModel
		interfaces = (relay.Node, )


class Product(SQLAlchemyObjectType):
	class Meta:
		model = ProductModel
		interfaces = (relay.Node, )

class Query(graphene.ObjectType):
	node = relay.Node.Field()
	all_products = SQLAlchemyConnectionField(Product)

schema = graphene.Schema(query=Query)

