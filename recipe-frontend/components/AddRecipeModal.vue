<template>
  <div
    class="relative z-10"
    aria-labelledby="modal-title"
    role="dialog"
    aria-modal="true"
    @click.stop
  >
    <!--
    Background backdrop, show/hide based on modal state.

    Entering: "ease-out duration-300"
      From: "opacity-0"
      To: "opacity-100"
    Leaving: "ease-in duration-200"
      From: "opacity-100"
      To: "opacity-0"
  -->
    <div
      class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
    ></div>

    <div class="fixed inset-0 z-10 overflow-y-auto">
      <div
        class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"
      >
        <!--
        Modal panel, show/hide based on modal state.

        Entering: "ease-out duration-300"
          From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          To: "opacity-100 translate-y-0 sm:scale-100"
        Leaving: "ease-in duration-200"
          From: "opacity-100 translate-y-0 sm:scale-100"
          To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
      -->
        <form @submit.prevent="handleSubmit">
          <div
            class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
          >
            <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div class="space-y-12">
                  <div class="border-b border-gray-900/10 pb-12">
                    <h2 class="text-base font-semibold leading-7 text-gray-900">
                      Add Recipe
                    </h2>
                    <div
                      class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6"
                    >
                      <div class="sm:col-span-4">
                        <label
                          for="recipe"
                          class="block text-sm font-medium leading-6 text-gray-900"
                          >Recipe name</label
                        >
                        <div class="mt-2">
                          <div
                            class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
                          >
                            <input
                              type="text"
                              name="recipe"
                              id="recipe"
                              autocomplete="recipe"
                              class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
                              placeholder="Recipe name"
                              v-model="form.recipe"
                              required
                            />
                          </div>
                        </div>
                      </div>

                      <div class="col-span-full">
                        <label
                          for="ingredients"
                          class="block text-sm font-medium leading-6 text-gray-900"
                          >Ingredients</label
                        >
                        <div class="mt-2">
                          <textarea
                            id="ingredients"
                            name="ingredients"
                            rows="3"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            v-model="form.ingredients"
                            required
                          ></textarea>
                        </div>
                      </div>

                      <div class="col-span-full">
                        <label
                          for="instructions"
                          class="block text-sm font-medium leading-6 text-gray-900"
                          >Instruction</label
                        >
                        <div class="mt-2">
                          <textarea
                            id="instructions"
                            name="instructions"
                            rows="3"
                            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                            v-model="form.instructions"
                            required
                          ></textarea>
                        </div>
                      </div>
                      <!-- For uploading recipe photo -->
                      <!-- <div class="col-span-full">
                        <label
                          for="photo"
                          class="block text-sm font-medium leading-6 text-gray-900"
                          >Photo</label
                        >
                        <div
                          class="mt-2 flex justify-center rounded-lg border border-dashed border-gray-900/25 px-6 py-10"
                        >
                          <div class="text-center">
                            <svg
                              class="mx-auto h-12 w-12 text-gray-300"
                              viewBox="0 0 24 24"
                              fill="currentColor"
                              aria-hidden="true"
                            >
                              <path
                                fill-rule="evenodd"
                                d="M1.5 6a2.25 2.25 0 012.25-2.25h16.5A2.25 2.25 0 0122.5 6v12a2.25 2.25 0 01-2.25 2.25H3.75A2.25 2.25 0 011.5 18V6zM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0021 18v-1.94l-2.69-2.689a1.5 1.5 0 00-2.12 0l-.88.879.97.97a.75.75 0 11-1.06 1.06l-5.16-5.159a1.5 1.5 0 00-2.12 0L3 16.061zm10.125-7.81a1.125 1.125 0 112.25 0 1.125 1.125 0 01-2.25 0z"
                                clip-rule="evenodd"
                              />
                            </svg>
                            <div
                              class="mt-4 flex text-sm leading-6 text-gray-600"
                            >
                              <label
                                for="file-upload"
                                class="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
                              >
                                <span>Upload a file</span>
                                <input
                                  id="file-upload"
                                  name="file-upload"
                                  type="file"
                                  class="sr-only"
                                />
                              </label>
                              <p class="pl-1">or drag and drop</p>
                            </div>
                            <p class="text-xs leading-5 text-gray-600">
                              PNG, JPG, GIF up to 10MB
                            </p>
                          </div>
                        </div>
                      </div> -->
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Toast -->
            <Success
              v-show="successState.success"
              :successText="successState.text"
              @close-save="successState.success = false"
            />
            <Error
              v-show="errorState.error"
              :errorText="errorState.text"
              @close-error="errorState.error = false"
            />
            <div
              class="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6"
            >
              <button
                type="submit"
                class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 sm:ml-3 sm:w-auto"
              >
                {{ props.isEditing ? "Edit" : "Add" }}
              </button>
              <button
                type="button"
                class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                @click="$emit('close-modal')"
              >
                Cancel
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { authStore } from "../stores/authStore";
import { ref } from "vue";
const auth = authStore();
const props = defineProps({
  refresh: {
    type: Function,
    required: true,
  },
  isEditing: {
    type: Boolean,
    required: false,
  },
  editData: {
    type: String,
    required: false,
  },
});
let form: any = props.isEditing
  ? JSON.parse(props.editData as string)
  : {
      recipe: "",
      ingredients: "",
      instructions: "",
      user: 0,
    };
let successState = reactive({ success: false, text: "" });
let errorState = reactive({ error: false, text: "" });

const handleSuccess = () => {
  form = {
    recipe: "",
    ingredients: "",
    instructions: "",
    user: 0,
  };
  successState.text = props.isEditing
    ? "Recipe edited successfully!"
    : "Recipe added successfully!";
  successState.success = true;
  props.refresh();
};

const handleSubmit = async () => {
  await auth.fetchUser();
  const user: any = auth.user;
  form.user = user.id;

  const { data, error }: any = !props.isEditing
    ? await useCustomFetch("recipe/", {
        method: "POST",
        body: form,
      })
    : await useCustomFetch("recipe/" + form.id + "/", {
        method: "PUT",
        body: form,
      });

  if (error.value == null) {
    handleSuccess();
  } else {
    errorState.text = error.value;
    errorState.error = true;
  }
};
</script>
