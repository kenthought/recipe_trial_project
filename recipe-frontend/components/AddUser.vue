<template>
  <div class="flex min-h-full flex-col justify-center lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm mt-2 py-3">
      <form @submit.prevent="register">
        <div>
          <label
            for="first_name"
            class="block text-sm font-medium leading-6 text-gray-900"
            >First name</label
          >
          <div class="mt-2">
            <input
              id="first_name"
              name="first_name"
              type="text"
              autocomplete="first_name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.first_name"
            />
          </div>
        </div>
        <div>
          <label
            for="middle_name"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Middle name</label
          >
          <div class="mt-2">
            <input
              id="middle_name"
              name="middle_name"
              type="text"
              autocomplete="middle_name"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.middle_name"
            />
          </div>
        </div>
        <div>
          <label
            for="last_name"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Last name</label
          >
          <div class="mt-2">
            <input
              id="last_name"
              name="last_name"
              type="text"
              autocomplete="last_name"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.last_name"
            />
          </div>
        </div>
        <div>
          <label
            for="email"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Email address</label
          >
          <div class="mt-2">
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.email"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Password</label
            >
          </div>
          <div class="mt-2">
            <input
              id="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.password"
            />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label
              for="password"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Confirm Password</label
            >
          </div>
          <div class="mt-2">
            <input
              id="confirm_password"
              name="confirm_password"
              type="password"
              required
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              v-model="form.confirm_password"
            />
          </div>
        </div>

        <div>
          <div class="mt-6 space-y-6">
            <div class="relative flex gap-x-3">
              <div class="flex h-6 items-center">
                <input
                  id="comments"
                  name="comments"
                  type="checkbox"
                  class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600"
                  v-model="form.is_superuser"
                />
              </div>
              <div class="text-sm leading-6">
                <label for="comments" class="font-medium text-gray-900"
                  >Add as admin</label
                >
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
        <div>
          <button
            type="submit"
            class="mt-5 flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Add user
          </button>
        </div>
      </form>
    </div>
  </div>
</template>
<script setup lang="ts">
const isEditing = useIsEditing();
const editData = useEditData();
let form: any = isEditing.value
  ? editData.value
  : {
      first_name: "",
      middle_name: "",
      last_name: "",
      email: "",
      username: "",
      password: "",
      confirm_password: "",
      is_staff: 1,
      is_admin: 1,
      is_superuser: 0,
    };
let successState = reactive({ success: false, text: "" });
let errorState = reactive({ error: false, text: "" });

const handleSuccess = () => {
  form = {
    first_name: "",
    middle_name: "",
    last_name: "",
    email: "",
    username: "",
    password: "",
    confirm_password: "",
    is_staff: 1,
    is_admin: 1,
    is_superuser: 0,
  };
  isEditing.value = false;
  editData.value = form;
  successState.text = isEditing
    ? "User edited successfully"
    : "User added successfully!";
  successState.success = true;
};

const register = async () => {
  console.log(form);
  if (form.password == form.confirm_password) {
    form.username = form.email;
    const temp: any = editData.value;
    const user_id: any = temp.id;

    const { data, error }: any = isEditing
      ? await useCustomFetch("users/" + user_id + "/", {
          method: "PUT",
          body: form,
        })
      : await useFetch("http://127.0.0.1:8000/api/users/register/", {
          method: "POST",
          body: form,
        });

    if (error.value == null) {
      handleSuccess();
    } else {
      errorState.text = error.value;
      errorState.error = true;
    }
  } else {
    errorState.text = "Password does not match!";
    errorState.error = true;
  }
};
</script>
