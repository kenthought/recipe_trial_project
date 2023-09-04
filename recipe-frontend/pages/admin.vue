<template>
  <div>
    <NuxtLayout :name="layout">
      <div>admin</div>
    </NuxtLayout>
  </div>
</template>
<script setup lang="ts">
import { definePageMeta } from "#imports";
const layout = "admin";

definePageMeta({
  middleware: ["auth"],
  layout: false,
});
</script>
