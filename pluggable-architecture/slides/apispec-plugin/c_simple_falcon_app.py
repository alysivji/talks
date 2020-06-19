import falcon

# Create Falcon web app
app = falcon.API()


class RandomPetResource:
    def on_get(self, req, resp):
        """A cute furry animal endpoint.
        ---
        description: Get a random pet
        responses:
            200:
                description: A pet to be returned
                schema: PetSchema
        """
        pet = None
        resp.media = pet


# create instance of resource
random_pet_resource = RandomPetResource()
# pass into `add_route` for Falcon
app.add_route("/random", random_pet_resource)
