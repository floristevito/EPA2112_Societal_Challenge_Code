<template lang="html">
  <div class="content">
    <div class="row no-gutters">
      <div id="empty1" class="col-md-0 col-xxl-1"></div>
      <div id="content" class="col-md-12 col-xxl-10">
        <!-- <router-view v-slot="{ Component }">
          <component :is="Component">
            <p>In Vue Router 3, I render inside the route component</p>
          </component>
        </router-view> -->

        <router-view></router-view>
      </div>
      <div id="empty2" class="col-md-0 col-xxl-1"></div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="css" scoped>
</style>
