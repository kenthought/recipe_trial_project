<template>
  <div v-if="pending">
    <p>Loading...</p>
  </div>
  <div v-else-if="error">
    <p>{{ error }}</p>
  </div>
  <div v-else>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead
        class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
      >
        <tr>
          <!-- <th scope="col" class="p-4">
            <div class="flex items-center">
              <input
                id="checkbox-all-search"
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="checkbox-all-search" class="sr-only"
                >checkbox</label
              >
            </div>
          </th> -->
          <th scope="col" class="px-6 py-3">First Name</th>
          <th scope="col" class="px-6 py-3">Middle Name</th>
          <th scope="col" class="px-6 py-3">Last Name</th>
          <th scope="col" class="px-6 py-3">Email</th>
          <th scope="col" class="px-6 py-3">Admin</th>
          <th scope="col" class="px-6 py-3">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
          v-for="item in users"
        >
          <!-- <td class="w-4 p-4">
            <div class="flex items-center">
              <input
                id="checkbox-table-search-1"
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="checkbox-table-search-1" class="sr-only"
                >checkbox</label
              >
            </div>
          </td> -->
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
          >
            {{ item.first_name }}
          </th>
          <td class="px-6 py-4">{{ item.middle_name }}</td>
          <td class="px-6 py-4">{{ item.last_name }}</td>
          <td class="px-6 py-4">{{ item.email }}</td>
          <td class="px-6 py-4">{{ item.is_superuser }}</td>
          <td class="flex items-center px-6 py-4 space-x-3">
            <a
              href="#"
              class="font-medium text-blue-600 dark:text-blue-500 hover:underline"
              @click="
                isEditing = true;
                editData = { ...item };
                usersTable = false;
                addUser = true;
              "
              >Edit</a
            >
            <a
              href="#"
              class="font-medium text-red-600 dark:text-red-500 hover:underline"
              @click="
                editData = { ...item };
                deleteUser = true;
              "
              >Remove</a
            >
          </td>
        </tr>
      </tbody>
    </table>
    <DeleteUser
      v-if="deleteUser"
      :refresh="refresh"
      @close-modal="deleteUser = false"
    />
  </div>
</template>
<script setup lang="ts">
const { data: users, pending, refresh, error }: any = useCustomFetch("users/");
const isEditing = useIsEditing();
const editData = useEditData();
const usersTable = useUsersTable();
const addUser = useAddUser();
const deleteUser = useDeleteUser();
</script>
